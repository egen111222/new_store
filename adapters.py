from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_login import current_user
from flask import url_for,redirect

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_app.login'))


class ImgView(AdminView):
    form_extra_fields = {
        'img': ImageUploadField(base_path="static")
    }

class CategoryView(ImgView):
    column_list = ("name","description","items","img")

class ItemView(ImgView):
    column_list = ("name","description","price","categories","img")

class OrderView(AdminView):
    column_list = ("id",
                   "username",
                   "phone_or_email",
                   "to_post",
                   "post_address",
                   "price",
                   "date",
                   "items")

