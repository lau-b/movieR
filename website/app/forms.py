from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    movie_title = StringField('movie title')
    submit = SubmitField('search ...')

