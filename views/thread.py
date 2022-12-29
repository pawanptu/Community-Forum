from flask import Blueprint, render_template
from flask_login import current_user
from . import models

thread = Blueprint('thread', __name__,
                   template_folder='templates')


# '/threadId' route and rendering thread.html according to I'd
@thread.route('/<string:threadId>')
def renderthreadPageFunction(threadId):
    threadObject = models.thread.query.filter_by(threadId=threadId).first()  # thread ID passed in url
    replysListLength = models.reply.query.filter_by(
        threadIdOfreply=threadId).count()
    if replysListLength == 0:
        return render_template('thread.html', user=current_user, thread=threadObject,
                               noreplys=True)
    else:
        replysList = models.reply.query.filter_by(
            threadIdOfreply=threadId).all()
        return render_template('thread.html', user=current_user, thread=threadObject, noreplys=False,
                               replys=replysList)
