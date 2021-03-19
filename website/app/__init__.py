from flask import Flask, render_template, request, url_for, jsonify, g
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db, Movies
from fuzzywuzzy import process


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


from .forms import SearchForm


@app.route('/')
def index():
    # add this to the session
    # also
    # load movies once and store
     # find out how to select title and id onlu
    return render_template('index.html')


@app.route('/top-movies')
def top_movies():
    result = Movies.query.filter(Movies.number_of_ratings > 50).order_by(Movies.avg_rating.desc()).limit(25).all()
    return render_template('top-movies.html', result=result)


@app.route('/rate-movies')
def rate_movies():
    form = SearchForm()
    return render_template('rate-movies.html', form=form)


@app.route('/recommendations')
def recommendations()
    return render_template('recommendations.html')

# this is just backend and not used in frontend
@app.route('/search_autocomplete')
def autocomplete():
    if 'lookup' not in g:
        g.movie_list = []
        g.lookup = Movies.query.filter(Movies.number_of_ratings > 50).all()
        for movie in g.lookup:
            g.movie_list.append(movie.title)

    matches = process.extractBests(request.args['term'],g.movie_list,limit=3)
    return jsonify([match[0] for match in matches])
