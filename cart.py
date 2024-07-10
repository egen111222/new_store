from models import Order
from models import db
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def create_order(self,form_data):
        order = Order(username=form_data.get("username"),
                      phone_or_email=form_data.get("phone_or_email"),
                      to_post=True if form_data.get("to_post") == "y" else False,
                      post_address=form_data.get("post_address"),
                      price=self.get_price())
        for item in self.items:
            order.items.append(item)
        db.session.add(order)
        db.session.commit()
        self.clear()
        return order
        
    def clear(self):
        self.items.clear()

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price

    def remove_item(self,number):
        self.items.pop(number)

    @property
    def numerated_items(self):
        return enumerate(self.items)

    def count(self):
        return len(self.items)

def get_cart(session):
    if "cart" not in session:
        session["cart"] = Cart()
    return session.get("cart")
