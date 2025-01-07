"""
Flask application for Emotion Detection.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_api():
    """
    Handles GET and POST requests to analyze emotions in a given text.

    Returns:
        str: A formatted response containing emotion scores and the dominant emotion.
    """
    text_to_analyze = ""  # Initialize the variable to avoid undefined usage

    if request.method == 'GET':
        # For GET, read the input text from query parameters
        text_to_analyze = request.args.get("textToAnalyze", "")
    elif request.method == 'POST':
        # For POST, read the input text from JSON body
        input_data = request.json
        text_to_analyze = input_data.get("text", "")

    # Validate input
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    # Process the input text with emotion_detector
    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response_text


@app.route('/')
def index():
    """
    Renders the index.html file for the web interface.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
