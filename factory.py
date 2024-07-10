from main import app
from models import db
from models import Item


def create_items(db,start,stop):
    for number in range(start,stop):
        item = Item(name=f"Товар {number}",
                    description=f"Опис {number}",
                    price=number * 10)
        db.session.add(item)
    db.session.commit()

with app.app_context():
    pass
    #create_items(db,1000,6000)
    #print("Виконано")
