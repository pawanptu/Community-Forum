from flask import Blueprint, render_template
from flask_login import current_user
from .models import Category, thread

category = Blueprint('category', __name__, template_folder='templates')


# '/categoryId' route and rendering category.html page according to I'd
@category.route('/<string:categoryId>')
def renderCategoryPageFunction(categoryId):
    categoryData = Category.query.filter_by(categoryId=categoryId).first()
    threadData = thread.query.filter_by(categoryId=categoryId)
    arethreadsNotThere = thread.query.filter_by(categoryId=categoryId).count()
    if arethreadsNotThere == 0:
        return render_template('category.html', user=current_user, category=categoryData, nothreads=True)
    else:
        return render_template('category.html', user=current_user, category=categoryData, threads=threadData,
                               nothreads=False)
