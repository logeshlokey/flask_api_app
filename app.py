from flask import Flask, jsonify
import os

app = Flask(__name__)

# Environment configuration
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

@app.route('/')
def home():
    return jsonify(message="Flask API running successfully on Render!")

@app.route('/health')
def health_check():
    return jsonify(status="healthy", service="Flask API", port=PORT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
