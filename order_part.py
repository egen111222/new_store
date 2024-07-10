from flask import (Blueprint,
                   render_template,
                   request,
                   session)
from cart import get_cart
from mail_lib import send_mail

order_app = Blueprint('order_app', __name__,
                      template_folder='templates')


@order_app.route("/create",methods=["GET","POST"])
def create_order():
    cart = get_cart(session)
    if request.method == "POST":
        form_data = request.form
        order = cart.create_order(form_data)
        message_text = order.message_text()
        send_mail(title=f"Замовлення № {order.id}",
                  body=message_text,
                  recipients=["labzin@ua.fm",
                              "ivan.kovbel@ex.ua",
                              "oleksandr.o.kuzmenko2@gmail.com",
                              "dmytro.bychek@gmail.com",
                              "egen11112222@gmail.com"])
        
        return render_template("thanks.html")
    return render_template("order.html")
