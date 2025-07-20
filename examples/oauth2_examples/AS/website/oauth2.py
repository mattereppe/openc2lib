from authlib.integrations.flask_oauth2 import (
    AuthorizationServer,
    ResourceProtector,
)
from authlib.integrations.sqla_oauth2 import (
    create_query_client_func,
    create_save_token_func,
    create_revocation_endpoint,
    create_bearer_token_validator,
)
from authlib.oauth2.rfc6749 import grants
from authlib.oauth2.rfc7636 import CodeChallenge
from authlib.oauth2.rfc7662 import IntrospectionEndpoint
from .models import db, User, OAuth2Client, OAuth2AuthorizationCode, OAuth2Token
import time


class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    TOKEN_ENDPOINT_AUTH_METHODS = [
        'client_secret_basic',
        'client_secret_post',
        'none',
    ]

    def save_authorization_code(self, code, request):
        code_challenge = request.data.get('code_challenge')
        code_challenge_method = request.data.get('code_challenge_method')
        auth_code = OAuth2AuthorizationCode(
            code=code,
            client_id=request.client.client_id,
            redirect_uri=request.redirect_uri,
            scope=request.scope,
            user_id=request.user.id,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )
        db.session.add(auth_code)
        db.session.commit()
        return auth_code

    def query_authorization_code(self, code, client):
        auth_code = OAuth2AuthorizationCode.query.filter_by(
            code=code, client_id=client.client_id).first()
        if auth_code and not auth_code.is_expired():
            return auth_code

    def delete_authorization_code(self, authorization_code):
        db.session.delete(authorization_code)
        db.session.commit()

    def authenticate_user(self, authorization_code):
        return User.query.get(authorization_code.user_id)


class MyIntrospectionEndpoint(IntrospectionEndpoint):
    def authenticate_endpoint_client(self, request):
        """
        Autentica il client che richiede l'introspection.
        """
        # Basic Auth (client_id + client_secret)
        auth = request.headers.get('Authorization')
        if auth and auth.startswith('Basic '):
            try:
                import base64
                credentials = base64.b64decode(auth[6:]).decode()
                client_id, client_secret = credentials.split(':', 1)
                client = OAuth2Client.query.filter_by(client_id=client_id).first()
                if client and client.check_client_secret(client_secret):
                    request.client = client
                    return client
            except Exception:
                pass  # autenticazione fallita

        request.client = None
        return None

    def query_token(self, token, token_type_hint):
        """Recupera il token dal database"""
        if not token:
            return None

        token = str(token).strip()

        if token_type_hint == 'access_token':
            return OAuth2Token.query.filter_by(access_token=token).first()
        elif token_type_hint == 'refresh_token':
            return OAuth2Token.query.filter_by(refresh_token=token).first()
        else:
            tok = OAuth2Token.query.filter_by(access_token=token).first()
            if not tok:
                tok = OAuth2Token.query.filter_by(refresh_token=token).first()
            return tok

    def introspect_token(self, token):
        """Return info about the token"""
        if not token:
            return {'active': False}

        expires_at = token.issued_at + token.expires_in
        is_active = (
                not token.is_token_revoked() and
                expires_at >= time.time()
        )

        result = {
            'active': is_active,
        }

        if is_active:
            result.update({
                'client_id': token.client_id,
                'token_type': getattr(token, 'token_type', 'Bearer'),
                'username': token.user.username if token.user else None,
                'scope': token.get_scope() if hasattr(token, 'get_scope') else None,
                'sub': str(token.user_id) if token.user_id else None,
                'aud': token.client_id,
                'iss': 'AS',
                'exp': int(expires_at),
                'iat': int(token.issued_at),
            })

            if token.user:
                result.update({
                    'email': getattr(token.user, 'email', None),
                    'email_verified': getattr(token.user, 'email_verified', False),
                })

        return result

    def check_permission(self, token, client, request):
        """
        Verifica se il client ha il permesso di fare introspection.
        """

        # Deve avere scope "introspect"
        if hasattr(client, 'has_scope') and not client.has_scope('introspect'):
            return False

        return True


class PasswordGrant(grants.ResourceOwnerPasswordCredentialsGrant):
    def authenticate_user(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            return user


class RefreshTokenGrant(grants.RefreshTokenGrant):
    def authenticate_refresh_token(self, refresh_token):
        token = OAuth2Token.query.filter_by(refresh_token=refresh_token).first()
        if token and token.is_refresh_token_active():
            return token

    def authenticate_user(self, credential):
        return User.query.get(credential.user_id)

    def revoke_old_credential(self, credential):
        credential.revoked = True
        db.session.add(credential)
        db.session.commit()


query_client = create_query_client_func(db.session, OAuth2Client)
save_token = create_save_token_func(db.session, OAuth2Token)
authorization = AuthorizationServer(
    query_client=query_client,
    save_token=save_token,
)
require_oauth = ResourceProtector()


def config_oauth(app):
    authorization.init_app(app)

    # support all grants
    authorization.register_grant(grants.ImplicitGrant)
    authorization.register_grant(grants.ClientCredentialsGrant)
    authorization.register_grant(AuthorizationCodeGrant, [CodeChallenge(required=True)])
    authorization.register_grant(PasswordGrant)
    authorization.register_grant(RefreshTokenGrant)

    # support revocation
    revocation_cls = create_revocation_endpoint(db.session, OAuth2Token)
    authorization.register_endpoint(revocation_cls)
    authorization.register_endpoint(MyIntrospectionEndpoint)

    # protect resource
    bearer_cls = create_bearer_token_validator(db.session, OAuth2Token)
    require_oauth.register_token_validator(bearer_cls())
