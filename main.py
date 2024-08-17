import os
import subprocess
import requests
import json

# Création du dépôt git
def initialize_git_repo():
    subprocess.run(["git", "init"], check=True)

# Effectuer un premier commit après ajout de fichier
def add_and_commit_files():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

# Création du dépôt distant
def create_remote_repo():
    GITHUB_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("Le token GitHub n'est pas défini dans l'environnement.")

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "M2_Exam_CVS"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Dépôt distant créé avec succès.")
    else:
        raise RuntimeError(f"Erreur lors de la création du dépôt distant : {response.status_code} {response.text}")

# Push au dépôt distant
def push_to_remote():
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/CarelBrian/ExoOVersioning.git"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

# Fonction main pour appeler toutes les fonctions précédentes
if __name__ == "__main__":
    initialize_git_repo()
    add_and_commit_files()
    create_remote_repo()
    push_to_remote()
