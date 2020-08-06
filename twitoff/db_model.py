"""SQLAlchemy models for twitoff
"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.Integer)

    def __repr__(self):
        return f'User: {self.username}'

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    #user = db.relationship('User', backref=db.backref('tweet', lazy=True))

    def __repr__(self):
        return f'Tweet: {self.text}'

# db.create_all() to make database