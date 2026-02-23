from flask import Flask, jsonify, request

# Instanciation de l'application Flask
app = Flask(__name__)

# Dictionnaire en mémoire pour stocker les utilisateurs
# ATTENTION : Il DOIT rester vide ici pour le checker Holberton !
users = {}

# ==========================================
# 1. Routes GET simples
# ==========================================

@app.route('/')
def home():
    """Endpoint racine"""
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    """Vérification du statut de l'API"""
    return "OK"

@app.route('/data')
def get_data():
    """Retourne la liste de tous les usernames (les clés du dictionnaire)"""
    return jsonify(list(users.keys()))

# ==========================================
# 2. Route GET dynamique
# ==========================================

@app.route('/users/<username>')
def get_user(username):
    """Retourne les détails d'un utilisateur spécifique"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# ==========================================
# 3. Route POST (Ajout de données)
# ==========================================

@app.route('/add_user', methods=['POST'])
def add_user():
    """Ajoute un nouvel utilisateur à partir de données JSON"""
    # silent=True évite que Flask crash violemment si le JSON est mal formaté
    data = request.get_json(silent=True)
    
    # 1. Vérification du format JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get("username")
    
    # 2. Vérification de la présence de la clé 'username'
    if not username:
        return jsonify({"error": "Username is required"}), 400
        
    # 3. Vérification des doublons
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # 4. Succès : Ajout au dictionnaire
    users[username] = data
    
    return jsonify({"message": "User added", "user": data}), 201

# Lancement du serveur de développement
if __name__ == "__main__":
    app.run()