from flask import Blueprint, flash, redirect
from flask_login import login_required, logout_user

logout = Blueprint('logout', __name__,
                   template_folder='templates')

# Logging User Out
@logout.route('/')
@login_required
def logoutUser():
    logout_user()
    flash("Logged Out Successfully", category='success')
    return redirect('/')
