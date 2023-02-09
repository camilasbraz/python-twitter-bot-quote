import os
import logging
from time import sleep
import time
import tweepy
from config import *
import traceback


from schedule import *
from get_quote import get_quote
from get_pic import get_pic

from datetime import date

today = date.today()
# dd/mm/YY
current_date = today.strftime("%d/%m/%Y")

#schedule()


logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

def initialize_api():
    api = CreateApi()
    return api

def tweetQuote(api):
    try:
        quote = get_quote()
        get_pic(quote)

        media = api.media_upload("result.jpg")

        api.update_status('Quote of the day ' + current_date,
                            media_ids=[media.media_id])
        
        logger.info('Quote of the day ' + current_date + " tweeted")
    except Exception as e:
        print(f'\Exception:\n{e}\n\n{traceback.format_exc()}\n\n')



       
def loop(api):
    while True:
        try:
            tweetQuote(api)
            time.sleep(time_to_wait * 3600)
        except Exception as e:
            print(f'\Exception:\n{e}\n\n{traceback.format_exc()}\n\n')
            time.sleep(600)
            continue


if __name__ == "__main__":
    api = initialize_api()
    loop(api)
