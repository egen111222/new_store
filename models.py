from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



category_item_table = db.Table("category_item_table",
                               db.Column("category_id",db.ForeignKey("categories.id")),
                               db.Column("items_id",db.ForeignKey("items.id"))
                               )
item_order_table = db.Table("item_order_table",
                            db.Column("items_id",db.ForeignKey("items.id")),
                            db.Column("order_id",db.ForeignKey("orders.id"))
                            )

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(250))
    phone_or_email = db.Column(db.String(250))
    to_post = db.Column(db.Boolean)
    post_address = db.Column(db.String(250))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime,default=datetime.now)
    items = db.relationship("Item",
                            secondary=item_order_table)

    def message_text(self):
        message_text = f"""Номер замовлення {self.id}
Від {self.username}
Контактні дані {self.phone_or_email}
Чи потрібна доставка {self.to_post}
Адреса доставки {self.post_address}
Загальна ціна замовлення {self.price}
Дата оформлення замовлення {self.date}
{'*'*20}\n"""
        for item in self.items:
            message_text += item.message_text()
            message_text += f"\n{'*'*20}\n"
        return message_text



class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    img = db.Column(db.String(200))
    categories = db.relationship("Category",
                                 secondary=category_item_table,
                                 back_populates="items")
    '''
    category_id = db.Column(db.ForeignKey("categories.id"))
    category = db.relationship("Category",
                               back_populates="items")
    '''
    def __str__(self):
        return self.name

    def message_text(self):
        message_text = f"""Назва товару {self.name}
Ціна товару {self.price}
"""
        return message_text


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer,
                   primary_key=True) 
    name = db.Column(db.String(150))
    description = db.Column(db.String(200))
    img = db.Column(db.String(200))
    items = db.relationship("Item",
                            secondary=category_item_table,
                            back_populates="categories")
    '''
    items = db.relationship("Item",
                            uselist=False)
    '''
    def __str__(self):
        return self.name
