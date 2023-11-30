from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

app = Flask(__name__)
CORS(app) 

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    messages = [
        {"role": "system", "content": "You are a kind helpful assistant."},
        {"role": "user", "content": user_message}
    ]
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo-1106", 
        messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role":"assistant","content":reply})
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(port=5000)
