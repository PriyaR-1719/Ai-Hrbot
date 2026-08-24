from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import generate_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "HR Chatbot Backend Running!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "No prompt provided"}), 400
    user_input = data["prompt"]
    answer = generate_response(user_input)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
