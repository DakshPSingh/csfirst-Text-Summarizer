import nltk

# Download required NLTK data
def download_nltk_data():
    print("Downloading NLTK data...")
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("NLTK data downloaded successfully!")
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

if __name__ == "__main__":
    download_nltk_data()
