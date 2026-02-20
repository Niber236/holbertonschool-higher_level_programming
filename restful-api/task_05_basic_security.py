from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt

app = Flask(__name__)
# Clé secrète pour signer les tokens (NE JAMAIS mettre en clair en prod)
app.config['JWT_SECRET_KEY'] = 'holberton-secret-key-2026'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Base de données en mémoire (Dictionnaire)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# ==========================================
# 1. BASIC AUTHENTICATION
# ==========================================
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized access"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

# ==========================================
# 2. JWT AUTHENTICATION (Login & Token generation)
# ==========================================
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # On injecte le rôle directement dans le token (Claims)
        access_token = create_access_token(identity=username, additional_claims={"role": user['role']})
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"error": "Bad username or password"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# ==========================================
# 3. ROLE-BASED ACCESS CONTROL (RBAC)
# ==========================================
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    # On récupère les infos stockées dans le token
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200

# ==========================================
# 4. CUSTOM JWT ERROR HANDLERS (Obligatoires pour le checker)
# ==========================================
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)