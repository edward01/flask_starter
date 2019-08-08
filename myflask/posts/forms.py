from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from myflask.posts.models import Post

class PostForm(FlaskForm):
    body = StringField('body', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(PostForm, self).__init__(*args, **kwargs)
        # self.post = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(PostForm, self).validate()
        if not initial_validation:
            return False

        # self.user = User.query.filter_by(username=self.username.data).first()
        # if not self.user:
        #     self.username.errors.append("Unknown username")
        #     return False

        # if not self.user.check_password(self.password.data):
        #     self.password.errors.append("Invalid password")
        #     return False

        # if not self.user.active:
        #     self.username.errors.append("User not activated")
        #     return False
        return True
