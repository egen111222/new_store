from models import db
from flask_login import UserMixin

class User(db.Model,
           UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True)
    login = db.Column(db.String(50))
    password = db.Column(db.String(256))
