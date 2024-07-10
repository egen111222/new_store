from models import db

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(150))
    phone_or_email = db.Column(db.String(250))
    text = db.Column(db.Text)
