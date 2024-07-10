from flask import Flask,render_template
from models import db
from models import Category,Item,Order
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from adapters import CategoryView,ItemView,AdminView,OrderView
from dotenv import load_dotenv
import os
from category_part import category_app
from item_part import item_app
from config_models import MenuElement
from conection_models import Message
from session_part import session_app
from flask_session import Session
from cart_part import cart_app
from order_part import order_app
from auth_models import User
from auth_lib import login_manager
from auth_part import auth_app
from mail_lib import mail
from mail_lib import send_mail
load_dotenv()

app = Flask(__name__,
            static_url_path="")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.config['FLASK_ADMIN_SWATCH'] = os.environ["FLASK_ADMIN_SWATCH"]
app.secret_key = os.environ["SECRET_KEY"]
app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]
app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = os.environ["MAIL_PORT"]
app.config["MAIL_USE_SSL"] = os.environ["MAIL_USE_SSL"]
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]

db.init_app(app)

Session(app)

login_manager.init_app(app)

mail.init_app(app)

with app.app_context():
    app.jinja_env.globals["menu_elements"] = MenuElement.query.all()
    db.create_all()


class UpdatedView(AdminView):
    def on_model_change(self,form, model, is_created):
        db.session.commit()
        with app.app_context():
            app.jinja_env.globals["menu_elements"] = MenuElement.query.all()

            
app.register_blueprint(category_app,
                       url_prefix="/categories")
app.register_blueprint(item_app)

app.register_blueprint(session_app,
                       url_prefix="/session")

app.register_blueprint(cart_app,
                       url_prefix="/cart")
app.register_blueprint(order_app,
                       url_prefix="/orders")

app.register_blueprint(auth_app,
                       url_prefix="/auth")

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html")


@app.errorhandler(404)
def user_error(e):
    return render_template("404.html")


admin = Admin(app, name='Наш Сайт', template_mode='bootstrap3')
admin.add_view(ItemView(Item, db.session))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(UpdatedView(MenuElement, db.session))
admin.add_view(AdminView(Message,db.session))
admin.add_view(OrderView(Order,db.session))
admin.add_view(AdminView(User,db.session))


app.run()
