import logging
import tweepy
import os
from keys import *

logger = logging.getLogger()

# Conecting to the API and returning the API object

def create_api():

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCES_TOKEN, ACCES_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")

    return api
