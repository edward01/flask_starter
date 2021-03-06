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
    session,
)
from flask_login import current_user, login_required

from ..extensions import login_manager
from ..utils import flash_errors
from ..public.forms import LoginForm
from ..user.models import User
from .forms import PostForm
from .models import Post

blueprint = Blueprint("posts", __name__, url_prefix="/posts", static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def index():
    current_app.logger.info("Hello from the posts page!")
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.get_by_id(current_user.get_id())
            Post.create(
                body=form.body.data,
                user=user,
            )
            flash("Blog created", "success")
            return redirect(url_for(".index"))
        else:
            flash_errors(form)
    form = LoginForm()
    posts = Post.query.all()
    return render_template("posts/index.html", form=form, posts=posts)


@blueprint.route("/add")
@login_required
def add():
    current_app.logger.info("Add page")
    form = PostForm()
    return render_template("posts/add.html", form=form)


@blueprint.route("/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit(post_id):
    current_app.logger.info("Hello from the posts edit page!")
    form = PostForm()
    post = Post.get_by_id(post_id)
    if request.method == "POST":
        if form.validate_on_submit():
            post.update(
                body=form.body.data,
            )
            flash("Blog updated", "success")
            return redirect(url_for(".edit", post_id=post.id))
        else:
            flash_errors(form)
    return render_template("posts/edit.html", form=form, post=post)
