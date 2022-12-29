# CREATE DATABASE MODELS

from datetime import datetime
from . import db
from flask_login import UserMixin


# Users Model
class User(db.Model, UserMixin):
    userName = db.Column(db.String(100), primary_key=True)
    realNameOfUser = db.Column(db.String(100), nullable=False)
    emailOfUser = db.Column(db.String(100), nullable=False, unique=True)  # unique emails in database
    passwordOfUser = db.Column(db.String(20), nullable=False)

    def get_id(self):
        return self.userName


# thread Model
class thread(db.Model):
    threadId = db.Column(db.String(100), primary_key=True)
    threadTitle = db.Column(db.String(250), nullable=False)
    threadDescription = db.Column(db.String(5000), nullable=False)
    userNameOfAsker = db.Column(db.String(1000), nullable=False)
    realNameOfAsker = db.Column(db.String(250), nullable=False)
    categoryId = db.Column(db.String(300), nullable=False)
    dateNow = db.Column(db.DateTime, default=datetime.utcnow())


# replys Model
class reply(db.Model):
    replyId = db.Column(db.String(100), primary_key=True)
    threadIdOfreply = db.Column(db.String(1000), nullable=False)
    replyDescription = db.Column(db.String(8000), nullable=False)
    userNameOfreplyer = db.Column(db.String(1000), nullable=False)
    realNameOfreplyer = db.Column(db.String(250), nullable=False)
    dateNow = db.Column(db.DateTime, default=datetime.utcnow())


# Category Models
class Category(db.Model):
    categoryId = db.Column(db.String(300), primary_key=True)
    categoryName = db.Column(db.String(1000), nullable=False)
    categoryDescription = db.Column(db.String(10000), nullable=False)
    categoryImage = db.Column(db.String(1000), nullable=True)

# insert into Category(categoryId, categoryName, categoryDescription, categoryImage) values('7', '', ' ', 'other-logo.png');
