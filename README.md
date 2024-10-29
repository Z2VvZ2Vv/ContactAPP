# ContactAPP
ContactAPP est une application de gestion de contacts. Elle permet aux utilisateurs de stocker et de gérer leurs informations de contact, telles que les noms, les numéros de téléphone, les adresses e-mail, etc. Elle permet également à l'utilisateur de chiffrer si elle le souhaite ses données avec une clé (algorithme de Fernet).

## Fonctionnalités

- Ajouter, modifier et supprimer des contacts
- Rechercher des contacts par nom
- Exporter les contacts vers un fichier ENC
- Gestion des erreurs et des interruptions de l'application
- Gestion du chiffrement

## Installation

1. Clonez le dépôt GitHub en utilisant la commande suivante : ```git clone https://github.com/Z2VvZ2Vv/ContactAPP.git```
   Ou télécharger le code source dans la release
3. Accédez au répertoire du projet : ```cd ContactAPP``` (par exemple)
4. Exécutez l'application en utilisant la commande suivante : ```python main_launcher.py``` (ou sur macOS/Linux ```python3 main_launcher.py```)

(!) Selon les configurations, le module ```cryptography```, de base sur python, peut ne pas être déployé. Donc si une erreur apparaît un simple ```pip install cryptography``` ```pip install pyreadline3``` sur Windows ou ```pip3 install cryptography``` sur macOS/Linux résoudra l'erreur !

## Screenshots

![alt text](https://raw.githubusercontent.com/Z2VvZ2Vv/ContactAPP/refs/heads/main/.assets/askingMenu.png)
--> Premier démarrage de l'application + demande à l'utilisateur s'il souhaite chiffrer ses données

![alt text](https://raw.githubusercontent.com/Z2VvZ2Vv/ContactAPP/refs/heads/main/.assets/key.png)
--> Découverte de la clé

![alt text](https://raw.githubusercontent.com/Z2VvZ2Vv/ContactAPP/refs/heads/main/.assets/mainMenu.png)
--> Menu principal de l'app


