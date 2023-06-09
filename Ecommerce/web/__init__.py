from flask import Flask, session
import mysql.connector


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'

    from .frontend.views import views as front_views
    from .frontend.auth import auth as front_auth
    from .backend.views import views as back_views
    from .backend.auth import auth as back_auth

    app.register_blueprint(front_views, url_prefix='/')
    app.register_blueprint(front_auth, url_prefix='/')
    app.register_blueprint(back_views, url_prefix='/admin/')
    app.register_blueprint(back_auth, url_prefix='/admin/')

    return app
