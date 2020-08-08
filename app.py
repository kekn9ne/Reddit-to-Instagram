from resize_image import resize
import config
import praw
import os
import random
import time
import urllib.request
from instabot import Bot

bot = Bot()
bot.login(username=config.instagram_username, password=config.instagram_password)

def bot_login():
    reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)
    return reddit

def bot_run(reddit, blacklist):
    subreddit = random.choice(config.subreddits)
    if config.post_type == "hot":
        submission = reddit.subreddit(subreddit).hot(limit=10)
    elif config.post_type == "top":
        submission = reddit.subreddit(subreddit).top(limit=10)
    elif config.post_type == "new":
        submission = reddit.subreddit(subreddit).new(limit=10)
    elif config.post_type == "rising":
        submission = reddit.subreddit(subreddit).rising(limit=10)
    else: 
        return print("Unknown post type. Edit post_type in config file.")

    for submission in submission:
        if submission.id not in blacklist and submission.url.endswith("jpg") or submission.url.endswith("jpeg") or submission.url.endswith("png"):
            print("Image found. Downloading.")

            urllib.request.urlretrieve(submission.url, submission.id + ".png")
            
            print("Image Downloaded. Uploading")

            resize(submission.id + ".png", 1080, 1080, submission.id)
            time.sleep(3)

            bot.upload_photo(submission.id + ".jpg", caption=config.post_caption.format(title=str(submission.title), author="u/" + str(submission.author), subreddit="r/" + str(submission.subreddit), score=str(submission.score)))

            blacklist.append(submission.id)
            with open("./blacklist.txt", "a") as f:
                f.write(submission.id + "\n")

            try:
                os.remove(submission.id + ".png")
                os.remove(submission.id + ".jpg.REMOVE_ME")
            except:
                return

            return
        else:
            continue

def get_blacklist():
    if not os.path.isfile("./blacklist.txt"):
            blacklist = []
    else:
        with open("./blacklist.txt", "r") as f:
            blacklist = f.read().split("\n")
    
    return blacklist

reddit = bot_login()
blacklist = get_blacklist()

while True:
    bot_run(reddit, blacklist)
    time.sleep(config.wait_before_posting)