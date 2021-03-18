from flask import Flask, render_template, request, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db, Movies, MoviesRating


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top-movies')
def top_movies():
    # result = (MoviesRating.query.filter_by(is_rated=True)).filter_by(number_of_ratings=10).order_by(MoviesRating.avg_rating.desc()).limit(10).all()
    result = MoviesRating.query.filter(MoviesRating.number_of_ratings > 50).order_by(MoviesRating.avg_rating.desc()).limit(25).all()
    return render_template('top-movies.html', result=result)


@app.route('/rate-movies')
def rate_movies():
    return render_template('rate-movies.html')
