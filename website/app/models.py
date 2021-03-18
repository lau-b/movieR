from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movies(db.Model):
    __tablename__ = 'movies_rating'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    published = db.Column(db.Integer)
    is_rated = db.Column(db.Boolean)
    avg_rating = db.Column(db.Float)
    number_of_ratings = db.Column(db.Integer)

    def __init__(self, title, published, is_rated, avg_rating, number_of_ratings):
        self.title = title
        self.published = published
        self.is_rated = is_rated
        self.avg_rating = avg_rating
        self.number_of_ratings = number_of_ratings

    def __repr__(self):
        return f'{self.title}:{self.avg_rating}'
