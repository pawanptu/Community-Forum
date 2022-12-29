from flask import Blueprint, request, flash, redirect
from flask_login import login_user
from .models import User
from werkzeug.security import check_password_hash
from .signup import checkEmail

login = Blueprint('login', __name__,
                  template_folder='templates')


# post requests of '/login/' to login user
@login.route('/', methods=['POST'])
def loginUser():
    emailIdUser = request.form['emailIdLogin']
    passwordLogin = request.form['passwordLogin']

    isEmailValid = checkEmail(emailIdUser)

    # If email of User is correct
    if isEmailValid:
        userObject = User.query.filter_by(
            emailOfUser=emailIdUser).first()

        if userObject:
            # Check user has typed correct password
            if check_password_hash(userObject.passwordOfUser, passwordLogin):
                loginSuccessful = login_user(userObject, remember=True)
                if loginSuccessful:
                    flash("Successfully Logged User In", category='success')
                else:
                    flash("Something went wrong while logging the user in", category='error')
                return redirect('/')

            else:
                flash("Invalid Credentials", category='error')
                return redirect('/')

        else:
            flash("Invalid Credentials", category='error')
            return redirect('/')

    else:  # If user email isn't valid
        flash("Email is not Valid", category='error')
        return redirect('/')
