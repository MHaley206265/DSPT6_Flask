from os import getenv
import basilica
import twitter_scraper
from dotenv import load_dotenv
from .db_model import db, User, Tweet


load_dotenv()
 
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))

def add_user_twitter_scraper(username):
    """Add a user and their tweets to database."""
    try:
        # Get user profile   
        user_profile = Profile(username)

        # Add user to table (or check if exists already)
        db_user = (User.query.get(user_profile.user_id) or
                    User(id=user_profile.user_id,
                        username=username,
                        followers=user_profile.followers_count))
        db.session.add(db_user)
        # Get most recent tweets
        tweets = list(get_tweets(username, pages=25))
        original_tweets = [d for d in tweets if d['username']==username]

        # add to tweet table
        for tweet in original_tweets:

            embedding = BASILICA.embed_sentence(tweet['text'], model='twitter')

            # add tweet info to tweet table
            db_tweet = Tweet(id=tweet.tweetId,
                            text=tweet.text[:300],
                            embedding=embedding)
        # Get an example Basilica embedding for first tweet
        
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    return user_profile, original_tweets, embedding