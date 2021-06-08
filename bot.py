#!/usr/bin/env

import tweepy
import glob
import random
import os
import time, datetime

class Work:
    def __init__(self, works, name):
        self.works = works
        self.name = name
                
def select_file():
    files = glob.glob("books/*")
    choice_1 = random.randint(1, len(files))

    if choice_1 == 1:
        poem = Work(glob.glob("books/Epicheski_pesni/*"), "Епически песни")
    else:
        raise Exception(f"Choice invalid: {choice_1};")

    choice_2 = random.randint(0, len(poem.works)-1)

    with open(poem.works[choice_2], "r", encoding='utf-8') as f:
        text = f.read()
        verse = text.split("\n\n")
        choice_3 = random.randint(0, len(verse)-1)
        post = verse[choice_3]
        while len(post) > 250:
            post = verse[random.randint(0, len(verse)-1)]
        return post, poem.name


def upload(verse, name):
    auth = tweepy.OAuthHandler(os.environ["oauth_key"], os.environ["oauth_secret"])
    auth.set_access_token(os.environ["access_key"], os.environ["access_secret"])
    api = tweepy.API(auth)
    api.update_status(f"{verse}\n\nиз '{name}'")
    api.send_direct_message("@_yamoz", f"I have uploaded on {datetime.datetime.now()}")


if __name__ == "__main__":
    while True:
        post, name = select_file()
        upload(post,name)
        print(f"Uploaded on {datetime.datetime.now()}\n")
        time.sleep(86400)
else:
    raise Exception("Cannot be imported")
