import os
import subprocess

# Création du dépôt git
def initialize_git_repo():
    subprocess.run(["git", "init"], check=True)

# Effectuer un premier commit après ajout de fichier
def add_and_commit_files():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

# Création du dépôt distant
def create_remote_repo():
    # Récupérer le token GitHub à partir des secrets
    GITHUB_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("Le token GitHub n'est pas défini dans l'environnement.")
    
    # Appeler l'API GitHub pour créer le dépôt
    result = subprocess.run([
        "curl",
        "-u",
        f"CarelBrian:{GITHUB_TOKEN}",
        "https://api.github.com/user/repos",
        "-d",
        '{"name":"M2_Exam_CVS"}'
    ], capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Erreur lors de la création du dépôt distant : {result.stderr}")
    print("Dépôt distant créé avec succès.")

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
