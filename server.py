"""
Flask web application for emotion detection using Watson NLP.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the homepage with input form for emotion detection.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """
    Handle requests for emotion detection.
    Accepts text input via GET or POST.
    Returns formatted string with emotion scores and dominant emotion.
    Handles invalid or blank inputs gracefully.
    """
    if request.method == "POST":
        text_to_analyse = request.form.get("text")
    else:
        text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
