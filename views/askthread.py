from flask import Blueprint, request, redirect, flash
from . import db
from .models import User
from .models import thread
import uuid

# Creating Blueprint to askthread endpoint
askthread = Blueprint('askthread', __name__,
                      template_folder='templates')


@askthread.route('/<string:profileUserName>', methods=['POST'])
def askthreadFunction(profileUserName):
    userData = User.query.filter_by(userName=profileUserName).first()
    askedthreadId = uuid.uuid4().hex
    askedthreadTitle = request.form['threadTitle']
    askedthreadDescription = request.form['threadDescription']
    askedthreadCategory = request.form['selectACategory']

    # Checking if thread is having a title and a description
    if len(askedthreadTitle) < 0 or len(askedthreadDescription) < 0:
        flash('The thread must have a title and a description',
              category='error')
        return redirect(
            f'/profile/{profileUserName}')
    else:
        newthread = thread(threadId=askedthreadId, threadTitle=askedthreadTitle,
                           threadDescription=askedthreadDescription, userNameOfAsker=profileUserName,
                           realNameOfAsker=userData.realNameOfUser,
                           categoryId=askedthreadCategory)

        try:
            db.session.add(newthread)
            db.session.commit()
            flash('thread Added Successfully', category='success')
            return redirect(f'/thread/{askedthreadId}')

        except:
            flash('Some Error Occured while adding the thread', category='error')
            return redirect(f'/profile/{profileUserName}')
