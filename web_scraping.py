import tweepy
import re
from nltk.corpus import stopwords
import nltk

#Authenticate User Key - Myat's Keys 
consumer_key = '90diU5nim8v4cUg0RFsdq6dqa'
consumer_secret = 'laShUmDF7tYMbX9Bk4F4u22FZiTIdzD6P84g7iiCh9rexzmLZD'
access_token = '905501172798296065-WnvOPmPn1URZa2GLsgaeJGd0FvTtki0'
access_token_secret = '4b4y3YW8broBjLGwcCVwWSfwHzcbr5dZqLMPE7zhl1Bzt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Define Search Words and Time Frame I Want to Search For 
search_words = "#andrewyang-filter:retweets" #filter out retweets 
from_date = "2019-10-01" #get tweets since from October 1st, 2019

#Collect the tweets
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=from_date).items(1000) #collecting first 1000 tweets that are in english language, the query is the search_words which is #andrewyang

#Compile it into a list 
all_tweets = [tweet.text for tweet in tweets]
#print(all_tweets)

#Clean the URL 
def clean_tweet(tweet):
    '''
    removes url and special chracters using regex
    '''
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split()) #replace the URL with nothing 

#save the cleaned tweets with for loop and create new list and append that 
cleaned_tweets = []
for tweet in all_tweets:
    tweet = clean_tweet(tweet)
    cleaned_tweets.append(tweet)
print(cleaned_tweets)

#Save the cleaned tweets onto a text file 
f = open("tweetslist_final.txt", "w")
new = [cleaned_tweets]
f.write("\n".join(map(lambda x: str(x), new)))
f.close()

