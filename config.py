import tweepy
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()


UNSPLASH_ACCESS_KEY = os.environ.get("ACCESS_KEY")

# Time in hours to wait to bot run 
time_to_wait = 24

def CreateApi():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info(f"API created! Connection to @{api.get_user(screen_name='felipeAmorinBot').name}")
    return api


