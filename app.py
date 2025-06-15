from flask import Flask, render_template, request
from summarizer.summarize import summarize_text
from sentiment.analyze import analyze_sentiment
from charts.word_stats import generate_wordcount_chart
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    sentiment = ""
    sentiment_keywords = []
    chart_generated = False
    original_text = ""
    summary_length = 3

    if request.method == "POST":
        original_text = request.form.get("original_text", "")
        summary_length = int(request.form.get("summary_length", 3))
        enable_sentiment = request.form.get("enable_sentiment") == "on"
        show_chart = request.form.get("show_chart") == "on"

        # Handle file upload
        if "upload_file" in request.files:
            file = request.files["upload_file"]
            if file and file.filename and file.filename.endswith('.txt'):
                file_content = file.read().decode("utf-8", errors="ignore")
                if file_content.strip():
                    original_text = file_content

        if original_text.strip():
            summary = summarize_text(original_text, summary_length)

            if enable_sentiment:
                sentiment_result = analyze_sentiment(original_text)
                sentiment = sentiment_result['sentiment']
                sentiment_keywords = sentiment_result['keywords']
            else:
                sentiment = None
                sentiment_keywords = []

            if show_chart:
                generate_wordcount_chart(original_text, summary)
                chart_generated = True

    return render_template("index.html",
                           original_text=original_text,
                           summary=summary,
                           sentiment=sentiment,
                           sentiment_keywords=sentiment_keywords,
                           summary_length=summary_length,
                           chart_generated=chart_generated)

if __name__ == "__main__":
    # Create static directory if it doesn't exist
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
