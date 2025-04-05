import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon (only once)
nltk.download('vader_lexicon')

# Sample tweets (you can replace with real ones)
tweets = [
    "I love the new design of the app!",
    "Ugh, this update is terrible.",
    "It’s okay, nothing special really.",
    "I’m so happy with the customer support!",
    "Worst service ever."
]

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment
results = []
for tweet in tweets:
    score = sia.polarity_scores(tweet)
    compound = score['compound']
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    results.append({"Tweet": tweet, "Sentiment": sentiment, "Score": compound})

# Display results
df = pd.DataFrame(results)
print(df)