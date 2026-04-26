from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper
import os

app = Flask(__name__)
CORS(app)  # permite acesso do GitHub Pages

model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["file"]

    os.makedirs("temp", exist_ok=True)
    filepath = os.path.join("temp", file.filename)
    file.save(filepath)

    result = model.transcribe(filepath)

    return jsonify({"text": result["text"]})

@app.route("/")
def home():
    return "API ONLINE 🚀"

if __name__ == "__main__":
    app.run()
