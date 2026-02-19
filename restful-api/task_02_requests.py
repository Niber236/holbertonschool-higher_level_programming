import requests
import csv

def fetch_and_print_posts():
    """Récupère les posts et affiche les titres."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Récupère les posts et les sauvegarde dans un fichier CSV."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # On structure les données (id, title, body)
        data_to_save = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']} 
            for p in posts
        ]
        
        # Écriture dans le fichier CSV
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_to_save)