
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return "Rezonanta: Yankı Sistemi Çalışıyor!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Soru eksik"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
