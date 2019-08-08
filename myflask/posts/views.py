# -*- coding: utf-8 -*-
"""Posts section"""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from myflask.extensions import login_manager
from myflask.utils import flash_errors
from .models import Post
from ..user.models import User

blueprint = Blueprint("posts", __name__, url_prefix="/posts", static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def index():
    current_app.logger.info("Hello from the posts page!")
    # Handle logging in
    if request.method == "POST":
        # if form.validate_on_submit():
        #     login_user(form.user)
        #     flash("You are logged in.", "success")
        #     redirect_url = request.args.get("next") or url_for("user.members")
        #     return redirect(redirect_url)
        # else:
        #     flash_errors(form)
        pass
    return render_template("posts/index.html")
