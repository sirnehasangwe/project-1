
"""
Sirneh Asangwe
Radical Software, Fall 2021
Project 1
Sept 23, 2021
python3
  """

import tweepy

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(MESSAGE_HERE)
print("Done.")
