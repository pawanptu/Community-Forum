from curses import flash
from flask import Blueprint, request, render_template, flash, redirect
from flask_login import current_user
from werkzeug.security import generate_password_hash
from .models import User, thread, Category
from . import db

profile = Blueprint('profile', __name__, template_folder='templates')


# '/profileId' route and rendering profile.html according to I'd
@profile.route('/<string:profileId>', methods=['GET', 'POST'])
def profilePageFunction(profileId):
    userObject = User.query.filter_by(userName=profileId).first()
    if request.method == 'POST':
        newNameOfUser = request.form['newRealName']
        newPasswordOfUser = request.form['newPassword']

        if len(newPasswordOfUser) < 5:
            flash('Password is too short, Please type a little long password', category='error')
            return redirect(f'/profile/{profileId}')

        else:
            newHashedPassword = generate_password_hash(newPasswordOfUser)
            userObject.realNameOfUser = newNameOfUser
            userObject.passwordOfUser = newHashedPassword
            try:
                db.session.add(userObject)
                db.session.commit()
                flash('Profile Successfully Edited', category='success')
                return redirect(f'/profile/{profileId}')
            except:
                flash('Some Error Occured while editing the profile, your profile may not have been changed',
                      category='error')
                return redirect(f'/profile/{profileId}')

    userthreads = thread.query.filter_by(userNameOfAsker=profileId).all()
    hasUserAskedthreads = thread.query.filter_by(userNameOfAsker=profileId).count()
    if hasUserAskedthreads == 0:
        return render_template('profile.html', user=current_user, profileUser=userObject, nothreads=True,
                               categoryData=Category.query.all())
    else:
        return render_template('profile.html', user=current_user, profileUser=userObject, userthreads=userthreads,
                               nothreads=False, categoryData=Category.query.all())  # Rendering HTML Page
