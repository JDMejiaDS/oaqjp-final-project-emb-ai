"""
Module to implement a Flask application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection import emo_detection

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    """
    Route to detect emotions based on the textToAnalyze parameter.
    """
    req = request.args.get("textToAnalyze")
    resp = emo_detection(req)
    if resp["dominant_emotion"] is None:
        return "Invalid text! Please try again."
    return f'''For the given statement, the system response is 'anger': {resp["anger"]},
    'disgust': {resp["disgust"]}, 'fear': {resp["fear"]},
    'joy': {resp["joy"]} and 'sadness': {resp["sadness"]}.
    The dominant emotion is {resp["dominant_emotion"]}.'''

@app.route("/")
def index_page():
    """
    Route to render the index.html template.
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, port=5000)
