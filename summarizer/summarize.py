from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import string

def split_into_sentences(text, word_threshold=25):
    """
    Hybrid sentence splitter: splits on punctuation, but if a sentence runs too long (word_threshold), force a split.
    Returns a list of sentences/chunks.
    """
    import re
    words = text.split()
    sentences = []
    current = []
    for word in words:
        current.append(word)
        if re.search(r'[.!?]$', word):
            sentences.append(' '.join(current).strip())
            current = []
        elif len(current) >= word_threshold:
            sentences.append(' '.join(current).strip())
            current = []
    if current:
        sentences.append(' '.join(current).strip())
    return [s for s in sentences if s]

def summarize_text(text, num_sentences=3):
    """
    Summarize the input text by extracting the most important chunks based on word frequency.
    Uses hybrid sentence splitting for robustness.
    Args:
        text (str): The input text to summarize.
        num_sentences (int): Number of chunks/sentences to include in the summary.
    Returns:
        str: The summary text.
    """
    import re
    if not text or not text.strip():
        return ""

    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import string

    sentences = split_into_sentences(text, word_threshold=25)
    if len(sentences) < num_sentences:
        return text.strip()

    # Tokenize words and compute frequency
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    freq = {}
    for word in words:
        if word not in stop_words:
            freq[word] = freq.get(word, 0) + 1

    # Score each sentence/chunk
    sentence_scores = {}
    for i, sent in enumerate(sentences):
        for word in word_tokenize(sent.lower()):
            if word in freq:
                sentence_scores[i] = sentence_scores.get(i, 0) + freq[word]

    # Select top N sentences/chunks
    ranked = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected = sorted([i for i, _ in ranked[:num_sentences]])
    summary = ' '.join([sentences[i] for i in selected])
    return summary.strip()