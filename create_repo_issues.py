#!/usr/bin/env python3
import argparse
import os
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
parser.add_argument("--issue1-title", "-t1", type=str, dest="issue1_title", required=True)
parser.add_argument("--issue1-body", "-b1", type=str, dest="issue1_body", required=True)
parser.add_argument("--issue2-title", "-t2", type=str, dest="issue2_title", required=True)
parser.add_argument("--issue2-body", "-b2", type=str, dest="issue2_body", required=True)
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private
issue1_title = args.issue1_title
issue1_body = args.issue1_body
issue2_title = args.issue2_title
issue2_body = args.issue2_body

GITHUB_USER = 'CarelBrian'  # Remplacez par votre nom d'utilisateur GitHub
GITHUB_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

def create_repo(name, is_private):
    payload = {
        "name": name,
        "private": is_private
    }
    headers = {
        "Authorization": "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(GITHUB_URL + "/user/repos", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la création du dépôt : {err}")
        print(f"Réponse : {response.text}")
        raise SystemExit(err)

def create_issue(repo_name, title, body):
    url = f'{GITHUB_URL}/repos/{GITHUB_USER}/{repo_name}/issues'
    payload = {
        'title': title,
        'body': body
    }
    headers = {
        "Authorization": "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la création du ticket : {err}")
        print(f"Réponse : {response.text}")
        raise SystemExit(err)

def init_git_repo(repo_name):
    os.makedirs(repo_name, exist_ok=True)
    os.chdir(repo_name)
    os.system("git init")
    os.system("git remote add origin https://github.com/" + GITHUB_USER + "/" + repo_name + ".git")
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system("git add . && git commit -m 'Initial Commit' && git push -u origin master")

def main():
    repo = create_repo(repo_name, is_private)
    print(f"Dépôt créé : {repo['html_url']}")

    init_git_repo(repo_name)

    issue1 = create_issue(repo_name, issue1_title, issue1_body)
    issue2 = create_issue(repo_name, issue2_title, issue2_body)
    
    print(f"Ticket 1 créé : {issue1['html_url']}")
    print(f"Ticket 2 créé : {issue2['html_url']}")

if __name__ == "__main__":
    main()
