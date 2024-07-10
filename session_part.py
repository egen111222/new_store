from flask import (Blueprint,
                   render_template)

from flask_login import login_required,current_user

session_app = Blueprint('session_app', __name__,
                        template_folder='templates')


@session_app.route("/")
@login_required
def secret_action():
    return render_template("session.html",
                           user=current_user)

