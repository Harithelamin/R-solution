from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

class FaqForm(FlaskForm):
    question = StringField('Question', validators=[InputRequired()])
    answer = StringField('Answer', validators=[InputRequired()])

class TopicForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = StringField('Content', validators=[InputRequired()])

class CommentForm(FlaskForm):
    comment = StringField('comment', validators=[InputRequired()])
    #topicId = IntegerField('topicId')
    #userId = IntegerField('userId')

class UserForm(FlaskForm):
    username = StringField('UserName', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    role = StringField('Role')

class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])

