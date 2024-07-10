from auth_models import User

class UserManager:
    def get_user_by_form(self,form_data):
        user = User.query\
               .filter(User.login == form_data.get("login"))\
               .filter(User.password == form_data.get("password"))\
               .first()
        return user

user_manager = UserManager()
