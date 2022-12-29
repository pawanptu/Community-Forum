from flask import Blueprint, request, flash, redirect
from flask_login import login_user
import re  # check an email of user
import uuid
from . import db
from .models import User
from werkzeug.security import generate_password_hash

signup = Blueprint('signup', __name__, template_folder='templates')


# post requests of '/signup/' to create a user account and login
@signup.route('/', methods=['POST'])
def signupUser():
    realNameOfUserSignup = request.form['realNameOfUser']
    userNameSignup = uuid.uuid4().hex
    print(userNameSignup)
    emailId = request.form['emailIdSignup']
    passwordOfUserSignup = request.form['passwordSignup']

    isEmailValid = checkEmail(emailId)

    # If email of User is correct
    if isEmailValid:
        doesEmailExists = User.query.filter_by(emailOfUser=emailId).first()

        if not doesEmailExists:
            newUser = User(userName=userNameSignup, realNameOfUser=realNameOfUserSignup, emailOfUser=emailId,
                           passwordOfUser=generate_password_hash(
                               passwordOfUserSignup))

            try:
                db.session.add(newUser)
                db.session.commit()
                login_user(newUser)
                flash("Account Created Successfully", category='success')
                return redirect('/')

            except:
                flash("Some Error Occured while creating an account", category='error')
                return redirect('/')
        else:
            flash("This email already exists. Please Login to access your account", category='error')
            return redirect('/')

    else:  # If user email isn't valid
        flash("Email is not Valid", category='error')
        print("Email is not Valid")
        return redirect('/')


def checkEmail(email):
    # check email of user and return true or false
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex, email):
        return True
    else:
        return False
