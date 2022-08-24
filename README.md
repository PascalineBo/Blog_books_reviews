# **OC_Projet9: Développez une application Web en utilisant Django**

## Objectif du projet: développer un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

#### Cahier des Charges:
[LITReview+-+Requirements+Specification (2).docx](https://github.com/MargueriteEffren/OC_Projet9/files/9416625/LITReview%2B-%2BRequirements%2BSpecification.2.docx)

#### Architecture du Projet:

Remarque: l'Appli utilise majoritairement Bootstrap 5 (https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css) pour la mise en forme

Le projet est découpé selon les dossiers suivants:
![image](https://user-images.githubusercontent.com/97900138/186423120-56183762-d63b-43da-81b0-139a77035cd2.png)

#### Dossier Authentication:
Ce dossier contient tous les fichiers de code définissant les interfaces et les procédés de sign up et de login:
![image](https://user-images.githubusercontent.com/97900138/186420168-f7883d05-7165-430b-9d4e-501680360069.png)

#### Dossier Blog:
Ce dossier contient tout les fichiers de code définissant les autres interfaces de l'Appli (page d'accueil, pages de créations de demande de critique et de rédaction,
page de suivi des abonnements...) et leurs procédés; il contient également le dossier static, avec un fichier css et un fichier js:

![image](https://user-images.githubusercontent.com/97900138/186420525-ea1e4f19-ae36-48b9-ab3b-ba33d1058743.png)

#### Dossier LITReview:
Ce dossier contient notamment les fichiers spécifiques settings.py et urls.py de l'Appli. 

![image](https://user-images.githubusercontent.com/97900138/186422141-546517f3-55f8-4705-96fb-690f56749063.png)

#### Dossier media:
Ce dossier stocke les images téléchargées par l'Appli

#### Dossier templates:
Ce dossier contient le fichier base.html, qui contient la partie de code html commune à toutes les pages de l'Appli

#### db.sqlite3:
C'est la base de données de Django

#### Fichier manage.py:
Ce fichier contient le script utilitaire de ligne de commande de Django

## Comment installer cette Appli sur votre ordinateur:
(i) Requis: téléchargez **[Python 3.10](https://www.python.org/downloads/)**

(ii) puis, avec les commandes du terminal, positionnez-vous sur le dossier dans lequel vous souhaitez installer l'Appli

(iii) pour importer les fichiers de ce repository, tapez la commande git:

git clone https://github.com/MargueriteEffren/OC_Projet9.git

(iv) puis positionnez vous dans le dossier OC_Projet9 (cd OC_Projet9)

(v) créez votre environnement virtuel, par exemple avec la commande:

python3 -m venv env

(vi) à l'aide des commandes du terminal, activez votre environnement virtuel 
(si votre environnement virtuel s'appelle env):
> Sur Windows  
- terminal de type bash : source env/Scripts/activate
- terminal de type shell : env\Scripts\activate
  
> Sur Mac ou Linux
- source env/bin/activate

(vii) puis installez les packages requirements du projet à l'aide de la commande:

$ pip install -r requirements.txt


## Comment utiliser l'Appli:

### Experience utilisateur:

(i) avec votre terminal, positionnez vous dans le dossier dans lequel vous avez installé l'Appli

(ii) activez l'environnement virtuel

(iii) ensuite tapez la commande 

$ python3 manage.py runserver

pour exécuter le serveur de développement

(iv) entrez dans votre navigateur l'adresse:

http://127.0.0.1:8000/

Vous devriez arriver sur la page de login. 

Essayer de vous connecter avec l'utilisateur:

username: toto

password: S3cret!

(v) pour arrêter l'exécution du serveur, faites Ctrl + C dans votre terminal.


### Experience administrateur:

(i) créez un compte super utilisateur avec la commande:

$ python3 manage.py createsuperuser

Suivez les instructions de l'invite pour créer votre superuser. Vous n'avez pas besoin de remplir une adresse électronique, 
mais n'oubliez pas votre mot de passe !

(ii) Ensuite, exécutez le serveur de développement, et dans votre navigateur, allez sur http://127.0.0.1:8000/admin/ 


