from flask import Flask
import mysql.connector

database = mysql.connector.connect(
    host='sql9.freemysqlhosting.net',
    port=3306,
    user='sql9607914',
    password='uWzaFxXgrH',
    database='sql9607914'
)

cursor = database.cursor()

cursor.execute('show all tables')


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
