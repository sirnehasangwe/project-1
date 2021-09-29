import tweepy


import random
message = ""

# option 1
# oneliner_list = ["peanut butter was never an option", "mayo is for the weak", "we only eat relish on the sabbath", "honeydew you love me", "I find this horse rather raddishing","poor kid mustard the whole thing from his bedroom"]

# message = random.choice(oneliner_list)


#Optoin 2: a simple mad lib

# string_template = "if life gave us {} then we can {}."
# word_list = [ "fruit", "firepower", "lightning", "exist", "obtain", "infer"]
# word1 = random.choice(word_list)
# word2 = random.choice(word_list)
# message = string_template.format(word1,word2)

from authorization_tokens import *

# Option 3: list of possible mad libs
#
# template_list = ["what good is {} if {} didn't happen", "how am I supposed to {} when they haven't {} yet", "Where did you get that {} and how do you use it with the {} inside of you"]
# word_list1 = ["butter", "happiness"]
# word_list2 = ["india", "now or never", "beginners luck", "jellyfisyhing"]
# template = random.choice(template_list)
# word1 = random.choice(word_list1)
# word2 = random.choice(word_list2)
#
# message = template.format(word1, word2)
#
# #option 4:using if statement

string_template = "Hi there, I'm {}, master of {}."

word_list1 = [ "Gritty", "Nicolas Cage" ]

word_list2_a = [ "monsters", "playing hockey", "scaring people" ]
word_list2_b = [ "movies", "acting", "saying 'woah'" ]

word1 = random.choice(word_list1)

if word1 == "Gritty":
    word2 = random.choice(word_list2_a)
elif word1 == "Nicolas Cage":
    word2 = random.choice(word_list2_b)

message = string_template.format(word1,word2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(message)
print("Done.")
