from flask import Blueprint, request, redirect, flash
from .models import reply
from . import db
import uuid
from flask_login import current_user

replythread = Blueprint('replythread', __name__,
                        template_folder='templates')


@replythread.route('/<string:threadId>', methods=['POST'])
def replythreadFunction(threadId):
    replyId = uuid.uuid4().hex
    replyDescription = request.form['replyOfthread']
    userNameOfreplyer = current_user.userName
    realNameOfreplyer = current_user.realNameOfUser

    if len(replyDescription) < 10:
        flash('The reply is too short, Please try to put at-least 10 characters', category='error')
        return redirect(f'/thread/{threadId}')
    else:
        replyObject = reply(replyId=replyId, threadIdOfreply=threadId, replyDescription=replyDescription,
                            userNameOfreplyer=userNameOfreplyer,
                            realNameOfreplyer=realNameOfreplyer)

        try:
            db.session.add(replyObject)
            db.session.commit()
            flash('Successfully replayed the thread', category='success')
            return redirect(f'/thread/{threadId}')
        except:
            flash('Some Error Occured', category='error')
            return redirect(f'/thread/{threadId}')
