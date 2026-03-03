from flask import Flask, request, send_file, redirect, url_for
import pyttsx3

app = Flask(__name__)

@app.route('/')
def home():
    # Serve your HTML file directly
    return send_file("index.html")

@app.route('/index.css')
def css():
    # Serve your CSS file directly
    return send_file("index.css")

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']

    engine = pyttsx3.init()
    engine.say(text)
    engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.runAndWait()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
