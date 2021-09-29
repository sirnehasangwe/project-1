import tweepy
import random
from authorization_tokens import *
import os, glob

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

message = ""

#Option 5: Basic Search

search_results = api.search_tweets(q="Africa Protests", lang="en")
# print(len(search_results))
# print( [ i.id for i in search_results ] )
search_result_tweet = random.choice(search_results)

# for tweet in tweepy.Cursor(api.search,
#                            q="Africa Protests",
#                            count=100,
#                            include_entities=True,
#                            lang="en").items():
#     print(tweet.created_at, tweet.text)
# exit()

# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(random_tweet._json)

text = search_result_tweet.text
message_list = ["Freeing yourself was one thing, claiming ownership of that freed self was another. #Africanlivesmatter",
    "Not everything that is faced can be changed, but nothing can be changed until it is faced.#Africanlivesmatter",
    "We must love each other and support each other. We have nothing to lose but our chains.#Africanlivesmatter",
    "For tomorrow belongs to the people who prepare for it today.#Africanlivesmatter",
    "There is no medicine to cure hatred.#Africanlivesmatter",
    "Wood already touched by fire is not hard to set alight.#Africanlivesmatter",
    "You never change things by fighting the existing reality. To change something, build a new model that makes the existing model obsolete.#Africanlivesmatter",
    "Education is the most powerful weapon which you can use to change the world.#Africanlivesmatter",
    "I dream of an Africa, which is in peace with itself.#Africanlivesmatter",
    "The water of the river flows on without waiting for the thirsty man.#Africanlivesmatter",
    "We have laid the foundation for a better life. Things that were unimaginable a few years ago have become everyday reality. I belong to the generation of leaders for whom the achievement of democracy was the defining challenge. #Africanlivesmatter",
    "Overcoming poverty is not a gesture of charity. It is an act of justice. It is the protection of a fundamental human right, the right to dignity and a decent life. While poverty persists, there is no true freedom.#Africanlivesmatter",
    "No one is born hating another person because of the color of his skin, or his background, or his religion.#Africanlivesmatter",
    "The very fact that racism degrades both the perpetrator and the victim commands that, if we are true to our commitment to protect human dignity, we fight on until victory is achieved.#Africanlivesmatter",
    "It is easy to break down and destroy. The heroes are those who make peace and build.#Africanlivesmatter",
    "Never be limited by other people’s limited imaginations.#Africanlivesmatter",
    "The cost of liberty is less than the price of repression.#Africanlivesmatter",
    "Hold fast to dreams, for if dreams die, life is a broken winged bird that cannot fly.#Africanlivesmatter",
    "We all have dreams. In order to make dreams come into reality, it takes an awful lot of determination, dedication, self-discipline and effort.#Africanlivesmatter",
    "I have learned over the years that when one’s mind is made up, this diminishes fear.#Africanlivesmatter",
    "He who is not courageous enough to take risks will accomplish nothing in life.#Africanlivesmatter",
    "Change will not come if we wait for some other person or some other time. We are the ones we’ve been waiting for. We are the change that we seek.#Africanlivesmatter"
    "#prayforAfrica",
    "https://www.gofundme.com/f/supporting-refugees-of-anglophone-crisis/donate",
    "#EndSARS",
    "#weshallovercome"]
message = random.choice(message_list)
print(message)

# print( dir(search_result_tweet) )

image_files = glob.glob("images/*")
# print(image_files)
image_file = random.choice(image_files)

# Upload image
media = api.media_upload(image_file)

# Post tweet with image
post_result = api.update_status(status=message, media_ids=[media.media_id])

#Option 6: mentions
# api.mentions_timeline
# mentions = api.mentions_timeline("@")
# mention_tweet = random.choice(mentions)
# thanks = " check out this beat while my dj revolves it."
message = "@" + search_result_tweet.user.screen_name + message
# pi.update_status(message, in_reply_to_status_id=mention_tweet.id)


#Option 7: working with other libraries
# api.update_status(message, in_reply_to_status_id=search_result_tweet.id)
# mentions = api.mentions_timeline()
# search_result_tweet = random.choice(mentions)
# search_result_tweet_words = search_result_tweet.text.split()
# word = random.choice(search_result_tweet)
# rhyming_word_list = pronouncing.rhymes(word)
# rhyme_word = random.choice(rhyming_word_list)
# template = "You say {Africa}, I say {head}."
# message = template.format(word,rhyme_word)
# message = "@" + mention_tweet.user.id
# api.update_status(message, in_reply_to_status_id=search_result_tweet.id)
# api.update_status(message)
print("Done.")
