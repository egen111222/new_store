from flask import Blueprint, render_template
from models import Item
from models import db
item_app = Blueprint('item_app', __name__,
                     template_folder='templates')


@item_app.route("/")
def view_items():
    items = db.paginate(Item.query,per_page=20)
    return render_template("items.html",
                           items=items)


@item_app.route("/<int:item_id>")
def view_item(item_id):
    item = Item.query.filter(Item.id == item_id).first()
    return render_template("item.html",
                           item=item)
