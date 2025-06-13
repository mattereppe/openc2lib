from website.app import create_app, run_app
import os

# Abilita il supporto a HTTP non sicuro 
os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

if __name__ == '__main__':

    print('starting app')
    app = create_app({
        'SECRET_KEY': 'secret',
        'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
    })
    run_app(app, port=9000)  
