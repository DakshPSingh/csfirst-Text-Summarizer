from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text using TextBlob and extract top sentiment keywords.
    Args:
        text (str): Input text to analyze (in English)
    Returns:
        dict: {'sentiment': str, 'keywords': list}
    """
    if not text or not text.strip():
        return {'sentiment': 'Neutral', 'keywords': []}
    from textblob import TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    # Classify sentiment based on polarity score
    if polarity > 0.1:
        sentiment = 'Positive'
    elif polarity < -0.1:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    # Extract keywords with highest absolute word polarity
    words = blob.words
    word_polarities = [(word, TextBlob(word).sentiment.polarity) for word in words]
    # Top 5 words by absolute polarity (not zero)
    keywords = [w for w, p in sorted(word_polarities, key=lambda x: abs(x[1]), reverse=True) if abs(p) > 0][:5]
    return {'sentiment': sentiment, 'keywords': keywords}

