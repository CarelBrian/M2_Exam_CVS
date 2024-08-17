"""
Concept des Git Worktrees

Les Git Worktrees permettent de travailler sur plusieurs branches en parallèle dans un seul dépôt sans avoir à cloner plusieurs fois le dépôt. Cela est particulièrement utile pour tester des fonctionnalités différentes ou corriger des bugs tout en continuant à travailler sur la branche principale.

### Utilisation des Git Worktrees

1. **Créer un Worktree**
   Pour créer un nouveau worktree, utilisez la commande suivante :
   ```bash
   git worktree add <chemin/vers/nouveau-worktree> <nom-de-branche>

   Par exemple, pour créer un worktree pour la branche feature-branch :

bash
git worktree add ../feature-branch feature-branch

Changer de Worktree
Vous pouvez travailler dans le nouveau worktree comme vous le feriez dans un dépôt normal. Accédez simplement au répertoire spécifié lors de la création du worktree.

Supprimer un Worktree
Pour supprimer un worktree, utilisez la commande :

bash
git worktree remove <chemin/vers/worktree>


Par exemple, pour supprimer le worktree créé précédemment :

bash
git worktree remove ../feature-branch


Lister les Worktrees
Pour voir tous les worktrees existants dans votre dépôt, utilisez :

bash
git worktree list


Exemple Pratique
Créez un nouveau worktree pour travailler sur une nouvelle fonctionnalité :

bash
git worktree add ../feature-branch feature-branch


Accédez au nouveau worktree :

bash
cd ../feature-branch
Effectuez des modifications et des commits dans le worktree sans affecter la branche principale.

Lorsque vous avez terminé, vous pouvez supprimer le worktree :

bash
git worktree remove ../feature-branch


Les worktrees simplifient le processus de gestion de plusieurs branches et permettent de garder un dépôt propre tout en travaillant sur plusieurs tâches simultanément.
"""