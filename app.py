from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "It always seems impossible until it’s done.",
    "The future belongs to those who prepare for it today.",
    "Dream big. Start small. Act now.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Push yourself, because no one else is going to do it for you."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_quote')
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)