import json
from flask import Flask, render_template

app = Flask(__name__)

# Routes existantes (Home, About, Contact)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# NOUVELLE ROUTE pour la Tâche 2
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # On récupère la liste associée à la clé "items"
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)