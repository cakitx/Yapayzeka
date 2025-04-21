from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Rezonanta API çalışıyor."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    # Geçici cevap mekanizması
    response = f"Sorduğun: '{question}'. Bu cevap test için oluşturulmuştur."

    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
