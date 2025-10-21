from flask import Flask, jsonify
import random

app = Flask(__name__)

# Some colorful messages to show
messages = [
    "🌈 Hello from Dockerized Flask app!",
    "🐳 Running strong inside Docker!",
    "🚀 Your container is alive and kicking!",
    "🔥 Flask + Docker = Magic!",
    "💻 Coded with love and Python!"
]

@app.route('/')
def hello():
    message = random.choice(messages)
    print(f"\033[92m[INFO]\033[0m Sending message: {message}")
    return jsonify(
        message=message,
        author="Mane Avagyan",
        container_status="✅ Running inside Docker",
        tip="Try refreshing for a new random message!"
    )

if __name__ == '__main__':
    print("\033[96m🚀 Starting Flask server on port 5000...\033[0m")
    print("\033[93mVisit: http://localhost:5000\033[0m")
    app.run(host='0.0.0.0', port=5000)

