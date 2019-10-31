import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
import matplotlib.pyplot as plt

f = open('tweetslist_final.txt').read()

# modify the text file so that each tweet appears as an item in the list for further sentiment analysis
tweets = f.split(', ') 


positive = 0
negative = 0
neutral = 0
total = 1000


# conduct sentiment analysis using nltk for each of the tweet
for item in tweets:
    score = SentimentIntensityAnalyzer().polarity_scores(item)
    # print(score) ## uncomment to see score for each of the 1000 tweets

    # determine the sentiment of the tweet based on its compound score 
    if score['compound'] > 0.05:
        positive += 1
    elif score['compound'] < -0.05:
        negative += 1
    else:
        neutral += 1


# calculate the percentage of positive, negative, and neutral tweets, then convert the numbers to a 100% scale with one decimal point
positive = float(format(positive/total*100, '.2f'))
negative = float(format(negative/total*100, '.2f'))
neutral = float(format(neutral/total*100, '.2f'))


# plot a pie chart that visualizes the percentage of each sentiment type
labels = ['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 
'Neutral ['+str(neutral)+'%]']
sizes = [positive, negative, neutral]
colors = ['blue','red','yellow']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("#andrewyang Tweets Sentiment Analysis")
plt.axis('equal')
plt.tight_layout()
plt.show()
