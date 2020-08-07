"""SQLAlchemy models for twitoff
"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.Integer)

    def __repr__(self):
        return f'User: {self.username}'

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    embedding = db.Column(db.PickleType, nullabe=False)
    #user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    #user = db.relationship('User', backref=db.backref('tweet', lazy=True))

    def __repr__(self):
        return f'Tweet: {self.text}'

# db.create_all() to make databases