import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

print('This is the start')
# Setting up the authentication


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# sentimental analysis
keyword = input('This program will analysis how people feel about certain thing on twitter \n'
                'Please enter the keyword to search:  ')
tweets = tweepy.Cursor(api.search, q=keyword).items(100)

positive = 0
negative = 0
neutral = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment.polarity > 0:
        positive += 1
    elif analysis.sentiment.polarity < 0:
        negative += 1
    else:
        neutral += 1
print(positive, negative, neutral)

# pie char for sentimental analysis

labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative, neutral]
explode = (0.1, 0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("On 100 tweets, how people feel about " + keyword)
plt.show()
