import tweepy
from textblob import TextBlob

consumer_key = "AfYZxxxxxxxxxxxxxxxxxx4yUFC"
consumer_secret = "1KEa6Zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxhk1TMny"

access_token = "144xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxHyiS"
access_token_secret = "BuoBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkExJin"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('india')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
