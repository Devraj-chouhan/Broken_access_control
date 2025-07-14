from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Simple in-memory user store (this will reset every time the server restarts)
users = {
    "rajesh01": "demopassword",
    "admin": "admin123"
}

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "Login successful", "redirect": "/dashboard.html", "token": "token123"})
    return jsonify({"success": False, "message": "Invalid credentials"})

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    username = request.json.get("username")
    if username in users:
        link = f"/reset-password.html?username={username}"  # Insecure and guessable
        return jsonify({"link": link})
    return jsonify({"error": "User not found"}), 404

@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    username = data.get("username")
    newpass = data.get("password")
    if username in users:
        users[username] = newpass
        return jsonify({"status": f"Password updated for {username}"})
    return jsonify({"error": "Invalid user"}), 400

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)
