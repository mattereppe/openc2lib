import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.sqla_oauth2 import (
    OAuth2ClientMixin,
    OAuth2AuthorizationCodeMixin,
    OAuth2TokenMixin,
)

# DEFINISCE I MODELLI DI DATABASE, CIOE LE TABELLE DEL DB.  

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(128))
    def __str__(self):
        return self.username

    def get_user_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class OAuth2Client(db.Model, OAuth2ClientMixin):
    __tablename__ = 'oauth2_client'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User')


class OAuth2AuthorizationCode(db.Model, OAuth2AuthorizationCodeMixin):
    __tablename__ = 'oauth2_code'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User')


class OAuth2Token(db.Model, OAuth2TokenMixin):
    __tablename__ = 'oauth2_token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User')

    def is_access_token_active(self):
        return (self.issued_at + self.expires_in) >= time.time()

    def is_refresh_token_active(self):
        refresh_expires_in = getattr(self, 'refresh_token_expires_in', 30 * 24 * 3600)
        return (self.issued_at + refresh_expires_in) >= time.time()

    def is_token_revoked(self):
        """Controlla se il token è stato revocato usando vari metodi possibili"""
        if hasattr(self, 'revoked'):
            return self.revoked
        if hasattr(self, 'is_revoked') and callable(self.is_revoked):
            return self.is_revoked()
        if hasattr(self, 'active'):
            return not self.active
        # Se non c'è informazione sulla revoca, assume che sia valido
        return False

