# Import SpaCy
import spacy
import pandas as pd
from textblob import TextBlob

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Loading the data
dataframe = pd.read_csv("amazon_product_reviews.csv")
reviews_data = dataframe['reviews.text']

# Remove missing values
clean_data = dataframe.dropna(subset=['reviews.text'])

# Function that performs sentiment analysis
def analyze_sentiment(review):
    # Remove stop words and perform data cleaning
    tokens = [token.text.lower().strip() for token in nlp(review) if not token.is_stop]
    cleaned_review = ' '.join(tokens)
    # Sentiment analysis using TextBlob
    blob = TextBlob(cleaned_review)
    sentiment_polarity = blob.sentiment.polarity
    
    # Determine the sentiment label based on the score
    if sentiment_polarity >= 0.1:
        sentiment = 'positive'
    elif sentiment_polarity <= -0.1:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment

# Testing the model
sample_reviews = ["This product is amazing!", "Not satisfied with the quality."]
for review in sample_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review}\nSentiment: {sentiment}\n")


# Choose two reviews for comparison
review_1 = dataframe['reviews.text'][0]
review_2 = dataframe['reviews.text'][1]

# Calculate similarity
similarity_score = nlp(review_1).similarity(nlp(review_2))

# Print the similarity score
print(f"Similarity Score between Review 1 and Review 2: {similarity_score}\n")