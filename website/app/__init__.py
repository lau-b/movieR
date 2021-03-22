from flask import Flask, render_template, request, url_for, jsonify, g, session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func
from .models import db, Movies
from fuzzywuzzy import process
import numpy as np


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

user_ratings_dict = {}

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
    results_list = []
    if len(request.args) != 0:
        search_title = str.lower(f"%{request.args['search_field']}%")
        search_results = Movies.query.filter(Movies.title.ilike(search_title)).order_by(Movies.published.asc()).all()
        for movie in search_results:
            results_list.append([movie.id, movie.title, movie.published])

    return render_template('rate-movies.html', results=results_list)


@app.route('/recommendations')
def recommendations():
    # import pickle
    # if 'nfm' not in session:
    #     with open('nfm.pickle', 'rb') as file:
    #         session['nmf'] = pickle.load(file)
    movies = Movies.query
    movie_dict = {}
    for movie in movies:
        movie_dict[movie.id] = 3.5
        # TODO: was ist wenn ich hier den average je movie einsetze?
        ## Könnte das direkt mit der Query holen.

    for element in session:
        movie_id = int(session[element][0])
        rating = float(session[element][1])
        movie_dict[movie_id] = rating
    # TODO: find a way to speed this up.
    ## maybe its fine to to this whole thing when clicking on 'get recs'

    return render_template('recommendations.html', movie_dict=movie_dict)

@app.route('/get_recs')
def get_recommendations():
    # load nmf
    # prepare movie_dict
    # get predictions
    # save them somewhere or return them.
    return '', 204

# this is just backend and not used in frontend
@app.route('/search_autocomplete')
def autocomplete():
    print(g)  # TODO: Malte => g seems to be destroyed after every request
    if 'lookup' not in g:
        g.movie_list = []
        print(g)
        g.lookup = Movies.query.filter(Movies.number_of_ratings > 50).all()
        for movie in g.lookup:
            g.movie_list.append(movie.title)

    matches = process.extractBests(request.args['term'], g.movie_list, limit=3)
    print(g, matches)
    return jsonify([match[0] for match in matches])

@app.route('/save_rating')
def save_rating():
    keys = request.args.keys()
    for key in keys:
        session[f'rating_{key}'] = ([key, request.args.__getitem__(key)])
        print(session)

    return '', 204  # returning '' and 204 prevents site from reloading
