from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genres = db.Column(db.String)

    def __init__(self, title, genre):
        self.title = title
        self.genres = genres

    def __repr__(self):
        return f'{self.genres}:{self.title}'
