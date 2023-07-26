import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sample social media data (tweets)
data = [
    "I love this product! It's amazing.",
    "The customer service was terrible.",
    "Neutral tweet about the brand.",
    # Add more data here...
]

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis
sentiments = []
for tweet in data:
    sentiment_score = sia.polarity_scores(tweet)
    sentiment = 'positive' if sentiment_score['compound'] >= 0.05 else 'negative' if sentiment_score['compound'] <= -0.05 else 'neutral'
    sentiments.append(sentiment)

# Print the results
for i, tweet in enumerate(data):
    print(f"Tweet: {tweet} | Sentiment: {sentiments[i]}")
