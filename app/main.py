from flask import Flask, jsonify
from app.greet import get_greeting

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": get_greeting("World")})

if __name__ == '__main__':
    print("Server running on http://127.0.0.1:5000")
    app.run(debug=True)
