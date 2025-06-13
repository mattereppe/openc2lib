import time
from flask import Blueprint, request, session, url_for
from flask import render_template, redirect, jsonify
from werkzeug.security import gen_salt
from authlib.integrations.flask_oauth2 import current_token
from authlib.oauth2 import OAuth2Error
from .models import db, User, OAuth2Client
from .oauth2 import authorization, require_oauth
import requests


bp = Blueprint('home', __name__)


def current_user():
    if 'id' in session:
        # print(session)
        uid = session['id']
        return User.query.get(uid)
    return None


def split_by_crlf(s):
    return [v for v in s.splitlines() if v]

from flask import request, jsonify
from .models import db, User
from sqlalchemy.exc import IntegrityError

#registrare user
@bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username') or request.json.get('username')
    password = request.form.get('password') or request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already taken'}), 409

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500

    return jsonify({'message': 'User created successfully'}), 201

# for web interface
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return render_template('login.html', error='Credenziali non valide')

        session['id'] = user.id

        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)

        return redirect('/')  # O un'altra pagina dopo il login

    return render_template('home.html')


@bp.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        username = request.form.get('username') or request.json.get('username')
        password = request.form.get('password') or request.json.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            print('cred invalide')
            return jsonify({'error': 'Invalid credentials'}), 401

        session['id'] = user.id

        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)

        return jsonify({"message": "Login successful"}), 200

    user = current_user()
    if user:
        print(user.id)
        clients = OAuth2Client.query.filter_by(user_id=user.id).all()
        return jsonify({
            "user": {"id": user.id, "username": user.username},
            "clients": [{"client_id": c.client_id, "client_name": c.client_metadata.get("client_name")} for c in clients]
        }), 200
    else:
        return jsonify({"error": "User not authenticated. Please log in."}), 401


@bp.route('/logout')
def logout():
    del session['id']
    return redirect('/')


@bp.route('/create_client', methods=('GET', 'POST'))
def create_client():
    user = current_user()
    if not user:
        return redirect('/')
    if request.method == 'GET':
        return render_template('create_client.html')

    client_id = gen_salt(24)
    client_id_issued_at = int(time.time())
    client = OAuth2Client(
        client_id=client_id,
        client_id_issued_at=client_id_issued_at,
        user_id=user.id,
    )

    form = request.form
    client_metadata = {
        "client_name": form["client_name"],
        "client_uri": form["client_uri"],
        "grant_types": split_by_crlf(form["grant_type"]),
        "redirect_uris": split_by_crlf(form["redirect_uri"]),
        "response_types": split_by_crlf(form["response_type"]),
        "scope": form["scope"],
        "token_endpoint_auth_method": form["token_endpoint_auth_method"]
    }
    client.set_client_metadata(client_metadata)

    if form['token_endpoint_auth_method'] == 'none':
        client.client_secret = ''
    else:
        client.client_secret = gen_salt(48)

    db.session.add(client)
    db.session.commit()
    return redirect('/')


@bp.route('/oauth/authorize', methods=['GET', 'POST'])
def authorize():
    user = current_user()
    # if user log status is not true (Auth server), then to log it in
    if not user:
        return redirect(url_for('home.home', next=request.url))
    if request.method == 'GET':
        try:
            grant = authorization.get_consent_grant(end_user=user)
            # print(grant)
        except OAuth2Error as error:
            print(error)
            return error.error

    if not user and 'username' in request.form:
        username = request.form.get('username') or request.json.get('username')
        user = User.query.filter_by(username=username).first()
        print(user)
    confirmed = True
    # confirmed = (
    # (request.form.get('confirm') == 'on') or
    # (request.json and request.json.get('confirm') in ['true', 'yes', True]))
    # print(confirmed)

    if confirmed:
        grant_user = user
    else:
        grant_user = None
    # input()
    # return jsonify({}),200
    a=authorization.create_authorization_response(grant_user=grant_user)
    status_code = a.status_code
    headers = a.headers
    content = a.data

    print(f"Status: {status_code}")
    print(f"Headers: {headers} {type(headers)}")
    print(f"Content: {content} {type(content)}")
    # return 200
    return jsonify(dict(headers)) #redirect con code al redirect_uri

@bp.route('/oauth/token', methods=['POST'])
def issue_token():
    # print('sono qui')
    a=authorization.create_token_response()
    return a

@bp.route('/oauth/introspect', methods=['POST'])
def introspect_token():
    response = authorization.create_endpoint_response('introspection')

    # print("Status code:", response.status_code)
    # print("Headers:", response.headers)
    # print("Body:", response.get_data(as_text=True))
    return response

@bp.route('/oauth/revoke', methods=['POST'])
def revoke_token():
    return authorization.create_endpoint_response('revocation')


@bp.route('/api/me')
@require_oauth('profile')
def api_me():
    user = current_token.user
    return jsonify(id=user.id, username=user.username)
