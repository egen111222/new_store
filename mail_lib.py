from flask_mail import Mail,Message

mail = Mail()


def send_mail(title="",
              body="",
              sender="ІНТЕРНЕТ_МАГАЗИН_НОВИЙ",
              recipients=[]):
    msg = Message(title,
                  body=body,
                  sender=sender,
                  recipients=recipients)
    mail.send(msg)
    

