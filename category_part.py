from flask import Blueprint, render_template
from models import Category

category_app = Blueprint('category_app', __name__,
                         template_folder='templates')


@category_app.route("/")
def view_categories():
    categories = Category.query.all()
    return render_template("categories.html",
                           categories=categories)


@category_app.route("/<int:category_id>")
def view_category(category_id):
    category = Category.query.filter(Category.id == category_id).first()
    return render_template("category.html",
                           category=category)
