import praw
import wget
import config

def logon():
    print("Logging on")
    return praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Meme Scraper tests v0.1")

def scrapeDaMemes(reddit):
    print("Scraping memes")
    for sub in config.subs:
        print("Scraping sub: " + sub)
        for submission in reddit.subreddit(sub).top(time_filter='day', limit=25):
            filetype = submission.url.split('.')[-1]
            if filetype in config.accepted_filetypes:
                wget.download(submission.url)

reddit = logon()
scrapeDaMemes(reddit)