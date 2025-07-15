from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

users = {
    "user": {"password": "user123", "role": "user"},
    "admin": {"password": "admin123", "role": "admin"}
}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and user["password"] == password:
        token = f"{user['role']}_token_123"
        redirect_url = "/admin.html" if user["role"] == "admin" else "/dashboard.html"
        return jsonify({"success": True, "token": token, "redirect": redirect_url})
    return jsonify({"success": False, "message": "Invalid credentials"})

@app.route('/check-admin', methods=['POST'])
def check_admin():
    token = request.json.get("token")
    if token == "admin_token_123":
        return jsonify({"access": "granted", "redirect": "/admin.html"})
    return jsonify({"access": "denied"})


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
