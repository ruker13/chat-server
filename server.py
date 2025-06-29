from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = {
        "username": data.get("username"),
        "text": data.get("text"),
        "time": datetime.now().strftime("%H:%M")
    }
    messages.append(message)
    return jsonify({"status": "ok"})

@app.route('/messages')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run()
