
from flask import Blueprint, flash, \
    redirect  # Importing Blueprint to handle routes related to request of the login of the website
from .models import thread  # Importing `thread` class from models.py to handle deleting of threads
from . import db  # Importing db from __init__.py to push changes in database
from flask_login import current_user, \
    login_required  # Importing current_use/r and login_required to get information about current user and checking if user has logged in before running deletethreadFunction

deletethread = Blueprint('deletethread', __name__,
                         template_folder='templates')


# Handling requests and deleting threads for specific thread ID's
@deletethread.route('/<string:threadId>')
@login_required
def deletethreadFunction(threadId):
    threadElement = thread.query.filter_by(
        threadId=threadId).first()

    try:
        db.session.delete(threadElement)
        db.session.commit()
        flash('Successfully deleted thread', category='success')
        return redirect(f'/profile/{current_user.userName}')
    except:
        flash('Some Error Occured, your thread might not have deleted', category='error')
        return redirect(f'/profile/{current_user.userName}')
