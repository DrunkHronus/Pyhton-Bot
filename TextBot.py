import praw
import time
import config_textbot

h = praw.Reddit(client_id = config_textbot.client_id,
                client_secret = config_textbot.client_secret,
                user_agent = "A test bot made by me",
                username = config_textbot.username, 
                password = config_textbot.password)
print(h.read_only)
print ("logging in...")

text_to_match = ["summon you"]
cache = []

def begin_bot():
    sub = h.subreddit("sandboxtest")
    print ("Subreddit opened")
    print(sub.title) 
    replies = sub.comments(limit=25)
    print ("Replies gathered")
    for reply in replies:
        reply_text = reply.body.lower()
        isSummoned = any(string in reply_text for string in text_to_match)
        if isSummoned and reply.id not in cache:
            print ("Summoned! Comment id: " + reply.id)
            reply.reply("Why hello there")
            print ("Replied")
            cache.append(reply.id)
    print ("Cycle done")

begin_bot()
