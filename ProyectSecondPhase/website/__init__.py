from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

dataBase = SQLAlchemy()
USER_NAME = 'sql9607914'
PASSWORD = 'uWzaFxXgrH'
HOST = 'sql9.freemysqlhosting.net'
PORT = 3306
DB_NAME = 'sql9607914'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

    dataBase.init_app(app)

    from .views import views
    from .auth import auth
    from .models.usermodel import User

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(Customer_id):
        return User.query.get(int(Customer_id))

    return app
