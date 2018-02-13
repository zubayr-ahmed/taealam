import tweepy
from textblob import TextBlob

consumer_key = "AfYZuGCup1sBXO7Xv00x4yUFC"
consumer_secret = "1KEa6Z63HDlqQuXMIkBCiM3NR5cksOZ9GoGzRQwRAOGhk1TMny"

access_token = "144773310-7EfM5mqrLLr3T0j05x5gieE1JkY1997NwxJMHyiS"
access_token_secret = "BuoBjnsXH8esAtwZWMznKDk3C4NsTYhWLlugREKkExJin"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

public_tweets = api.search('india')

for tweet in public_tweets:
    print tweet.text
    analysis = TextBlob(tweet.text)
    print analysis.sentiment

