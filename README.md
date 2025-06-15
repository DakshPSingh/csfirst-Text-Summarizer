# Text Analysis Web Application

A Flask-based web application that provides text analysis features including summarization, sentiment analysis, and word statistics.

## Features

- Text summarization
- Sentiment analysis
- Word statistics and frequency analysis
- Responsive web interface

## Prerequisites

- Python 3.9+
- pip (Python package manager)

## Setup Instructions

1. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to: `http://localhost:5000`

## Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t text-analysis-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 text-analysis-app
   ```

3. **Access the application**:
   Open your web browser and go to: `http://localhost:5000`

## Project Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
  - `index.html`: Main web interface
- `summarizer/`: Text summarization module
  - `summarize.py`: Summarization logic
- `sentiment/`: Sentiment analysis module
  - `analyze.py`: Sentiment analysis logic
- `charts/`: Word statistics module
  - `word_stats.py`: Word analysis logic
- `static/`: Static files (CSS, JS, images)
- `Dockerfile`: Docker configuration
- `requirements.txt`: Python dependencies

## License

This project is open source and available under the [MIT License](LICENSE).
