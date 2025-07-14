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
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and user["password"] == password:
        # Generate correct token based on role
        role = user["role"]
        token = f"{role}_token_123"  # e.g., user_token_123 or admin_token_123

        return jsonify({
            "success": True,
            "token": token,
            "redirect": "/dashboard.html"
        })
    else:
        return jsonify({
            "success": False,
            "message": "Invalid credentials"
        })


    user = users.get(username)
    if user and user["password"] == password:
        token = f"{user['role']}_token_123"
        return jsonify({"success": True, "token": token, "redirect": "/dashboard.html"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})

@app.route('/check-admin', methods=['POST'])
def check_admin():
    token = request.json.get("token")
    if token == "admin_token_123":
        return jsonify({"access": "granted", "redirect": "/admin.html"})
    return jsonify({"access": "denied"})

# ❌ REMOVE THIS CONFLICTING ROUTE
# @app.route('/<path:filename>')
# def serve_static_file(filename):
#     return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(debug=True)
