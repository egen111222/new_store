from wtforms_alchemy import ModelForm
from models import Order
from auth_models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ["price"]


class UserForm(ModelForm):
    class Meta:
        model = User
