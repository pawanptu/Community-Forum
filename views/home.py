from flask import Blueprint, render_template
from flask_login import current_user
from .models import Category

home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


# Rendering home.html page for '/' route
@home.route('/')
def renderHomePage():
    # var1 = Category(categoryId='1',categoryName='Python',categoryDescription="Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects",categoryImage='python-logo.png')
    # db.session.add(var1)
    # db.session.commit()
    return render_template('home.html', user=current_user, categories=Category.query.all())
