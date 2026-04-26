from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    هذه الدالة تستقبل النص من الواجهة، ترسلها للتحليل،
    وتعيد النتيجة بالتنسيق المطلوب من العميل.
    """
    # الحصول على النص من الطلب (Request)
    text_to_analyze = request.args.get('textToAnalyze')
    
    # تحليل النص باستخدام الدالة التي أنشأناها في الحزمة
    response = emotion_detector(text_to_analyze)
    
    # استخراج القيم من النتيجة
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # التنسيق المطلوب من العميل بدقة (Format the output)
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    هذه الدالة تقوم بعرض الصفحة الرئيسية للموقع.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # تشغيل التطبيق على localhost والمنفذ 5000
    app.run(host="0.0.0.0", port=5000)