#!/usr/bin/env python

import argparse
import logging
import praw
import os

CLIENT_ID = os.environ['OFFICE-BOT-CLIENT-ID']
CLIENT_SECRET = os.environ['OFFICE-BOT-CLIENT-SECRET']
USERNAME = os.environ['OFFICE-BOT-USERNAME']
PASSWORD = os.environ['OFFICE-BOT-PW']
USER_AGENT = os.environ['OFFICE-BOT-USER-AGENT']
CULPRIT = 'Assistant Regional Manager'
REPLY_TEXT = 'Assistant *to* the Regional Manager^(I am a bot, beep boop |) [^(Github)](https://github.com/colinrlly/assistant-to-the-regional-manager-bot) ^(|) [^(My Father)](http://www.colin.world/)'


def main():
    # Setup logging
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger('prawcore')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Create a new praw instance
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT,
                         username=USERNAME,
                         password=PASSWORD)

    # Your code goes here ...
    # dunder_mifflin = reddit.subreddit('DunderMifflin')
    # for comment in dunder_mifflin.stream.comments():
    for comment in reddit.submission(id='98nh50').comments.list():
        # print(submission.title)
        # all_comments = submission.comments.list()
        # for comment in all_comments:
        try:
            if CULPRIT in comment.body:
                print('-------------------------')
                print(comment.body)
                print('replying')
                comment.reply(REPLY_TEXT)
                print('-------------------------')
        except:
            pass


if __name__ == "__main__":
    # Command line arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '-b', '--bot',
    #     required=False,
    #     default='bot1',
    #     help='Name of the bot to use from praw.ini. Default: bot1'
    # )
    # args = parser.parse_args()

    main()