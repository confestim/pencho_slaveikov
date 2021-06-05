#!/usr/bin/env

import tweepy
import glob
import random
import os
import time, datetime

def select_file():
    works = []
    files = glob.glob("books/*")
    choice_1 = random.randint(1, len(files))

    if choice_1 == 1:
        works = glob.glob("books/Epicheski_pesni/*")
        name = "Епически песни"
    else:
        raise Exception(f"Choice invalid: {choice_1};")

    choice_2 = random.randint(0, len(works)-1)
    with open(works[choice_2], "r", encoding='utf-8') as f:
        text = f.read()
        verse = text.split("\n\n")
        choice_3 = random.randint(0, len(verse)-1)
        post = verse[choice_3]
        while len(post) > 250:
            post = verse[random.randint(0, len(verse)-1)]

        return post, name


def upload(verse, name):
    auth = tweepy.OAuthHandler(os.environ["oauth_key"], os.environ["oauth_secret"])
    auth.set_access_token(os.environ["access_key"], os.environ["access_secret"])

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(f"{verse}\n\nиз '{name}'")
# if __name__ == "__main__":


while True:
    post, name = select_file()
    upload(post,name)
    print(f"Uploaded on {datetime.datetime.now()}\n")
    time.sleep(86400)