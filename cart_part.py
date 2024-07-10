from flask import (Blueprint,
                   render_template,
                   session,
                   redirect,
                   url_for)
from models import Item
from cart import get_cart
from forms import OrderForm

cart_app = Blueprint('cart_app', __name__,
                     template_folder='templates')


@cart_app.route("/")
def view_cart():
    form = OrderForm()
    cart = get_cart(session)
    return render_template("cart.html",
                           cart=cart,
                           form=form)
    
@cart_app.route("/add/<int:item_id>")
def add_item(item_id):
    item = Item.query.filter(Item.id == item_id).first()
    cart = get_cart(session)
    cart.add_item(item)
    return redirect(url_for('cart_app.view_cart'))

@cart_app.route("/remove/<int:item_id>")
def remove_item(item_id):
    cart = get_cart(session)
    cart.remove_item(item_id)
    return redirect(url_for('cart_app.view_cart'))


