import os
import requests
import json
import subprocess

# Création du dépôt distant
def create_remote_repo():
    GITHUB_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("Le token GitHub n'est pas défini dans l'environnement.")

    repo_name = "M2_Exam_CVS"  # Changez ce nom si le dépôt existe déjà
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    payload = {
        "name": 'M2_Exam_CVS'
    }

    # Vérifier si le dépôt existe déjà
    check_url = f"https://api.github.com/repos/CarelBrian/{repo_name}"
    response = requests.get(check_url, headers=headers)
    if response.status_code == 200:
        print("Le dépôt existe déjà.")
        return

    # Créer le dépôt si il n'existe pas
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Dépôt distant créé avec succès.")
    else:
        raise RuntimeError(f"Erreur lors de la création du dépôt distant : {response.status_code} {response.text}")

# Initialiser le dépôt Git
def initialize_git_repo():
    subprocess.run(["git", "init"], check=True)

# Effectuer un premier commit après ajout de fichier
def add_and_commit_files():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

# Push au dépôt distant
def push_to_remote():
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/CarelBrian/M2_Exam_CVS.git"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

# Fonction principale pour appeler toutes les fonctions précédentes
if __name__ == "__main__":
    initialize_git_repo()
    add_and_commit_files()
    create_remote_repo()
    push_to_remote()
