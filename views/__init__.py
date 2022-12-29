# CONNECT DATABASE

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()  # Creating Database
DATABASENAME = 'CommunityForum.db'


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'flaskcommunity'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASENAME}'
    db.init_app(app)  # Adding App in Database

    # Importing home from home.py to address '/' route of website

    from .home import home
    from .category import category
    from .thread import thread
    from .profile import profile
    from .askthread import askthread
    from .signup import signup
    from .login import login
    from .logout import logout
    from .deletethread import deletethread
    from .replythread import replythread

    # Registering Blueprint for pages so that pages are called then code of that pages are used
    app.register_blueprint(home, url_prefix="/")

    app.register_blueprint(category, url_prefix="/category")

    app.register_blueprint(thread, url_prefix="/thread")

    app.register_blueprint(profile, url_prefix="/profile")

    app.register_blueprint(askthread, url_prefix="/askthread")

    app.register_blueprint(signup, url_prefix="/signup")

    app.register_blueprint(login, url_prefix="/login")

    app.register_blueprint(logout, url_prefix="/logout")

    app.register_blueprint(deletethread, url_prefix="/deletethread")

    app.register_blueprint(replythread, url_prefix="/replythread")

    createDatabase(app)  # it create database if it doesn't exists

    loginManagerVariable = LoginManager()
    loginManagerVariable.login_view = 'login.loginUser'
    loginManagerVariable.init_app(app)

    from .models import User

    @loginManagerVariable.user_loader
    def loadUser(userName):
        return User.query.get(str(userName))

    # Return Database to run app.py
    return app


def createDatabase(app):
    if not path.exists('views/' + DATABASENAME):
        db.create_all(app=app)
        print('Created Database!')
