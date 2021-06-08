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

def authenticate():
    auth = tweepy.OAuthHandler(os.environ["oauth_key"], os.environ["oauth_secret"])
    auth.set_access_token(os.environ["access_key"], os.environ["access_secret"])
    api = tweepy.API(auth)
    return api

def check_tweets(verse):
    api = authenticate()
    tweets = api.user_timeline()
    for i in tweets:
        text = i.text.split("https://")
        text = text[0].split("...")
        text = text[0]
        if text in verse:
            raise Exception("Already tweeted")

def upload(verse, name):
    try:
        api.update_status(f"{verse}\n\nиз '{name}'")
        api.send_direct_message(2885504686, f"I have uploaded on {datetime.datetime.now()}")
        check_tweets(verse)
        return
    except Exception as e:
        api.send_direct_message(2885504686, f"I've already posted\nError:{e}")
        pass

if __name__ == "__main__":
    while True:
        time.sleep(5)
        verse, name = select_file()
        upload(verse,name)
        time.sleep(43200)
else:
    raise Exception("Cannot be imported")
