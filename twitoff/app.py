from flask import Flask, render_template
from .db_model import db, User

def create_app():
    """Create and configure an instance of the Flask App
    """

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D:\\git_repos\\Unit3\\sprint3\\DSPT6_Flask\\twitoff\\twitoff.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    return app