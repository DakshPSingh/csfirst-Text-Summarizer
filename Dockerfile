# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies for matplotlib, nltk, etc.
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download required NLTK data at build time
RUN python3 -m nltk.downloader -d /usr/local/nltk_data punkt punkt_tab stopwords
ENV NLTK_DATA=/usr/local/nltk_data

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables for production
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Use gunicorn for production serving
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
