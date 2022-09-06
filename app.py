"""

A twitter bot that posts random dogs every 20 minutes.

Created with tweepy API for twitter actions.
Uses random.dog API to get the random dogs media.
Uses logging to log the actions.

Is a basic bot, but it works well. You can keep it running on a server or on your computer.

"""

import requests
import tweepy
import logging
import json
import urllib.request
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def app(api):
    # Define API
    url = "https://random.dog/woof.json"

    # Call the API
    response = requests.get(url)

    if response.status_code == 200:
        # Get the image URL
        url_media = response.json()['url']

        # Get the media extension, download and upload it
        if url_media.endswith(".mp4" or ".gif"):

            urllib.request.urlretrieve(url_media, "./media/video.mp4")
            upload_media("./media/video.mp4", api)
        else:

            with open('./media/image.jpg', 'wb') as f:
                f.write(requests.get(url_media).content)
                upload_media("./media/image.jpg", api)


def upload_media(media_url, api):

    # Uploading the media
    try:
        media = api.media_upload(media_url)

        result = api.update_status(status="", media_ids=[
                                   media.media_id_string])
        print("Media uploaded")
    except:
        print("Error during the upload")


def main():
    api = create_api()

    while True:
        app(api)
        logger.info("Waiting...")
        time.sleep(1200)


if __name__ == "__main__":
    main()
