from flask import Flask, render_template, request

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # هذا السطر سيطبع الرسالة فوراً مهما كان النص
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)