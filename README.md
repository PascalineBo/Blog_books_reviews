# **OC_Projet9: Développez une application Web en utilisant Django**

## Objectif du projet: développer un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

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
(i) Requis: téléchargez **Python 3.10**
https://www.python.org/downloads/

(ii) puis, avec les commandes du terminal, positionnez-vous sur le dossier dans lequel vous souhaitez installer l'Appli

(iii) créez votre environnement virtuel

(iv) à l'aide des commandes du terminal, activez votre environnement virtuel 
(si votre environnement virtuel s'appelle env):
> Sur Windows  
- terminal de type bash : source env/Scripts/activate
- terminal de type shell : env\Scripts\activate
  
> Sur Mac ou Linux
- source env/bin/activate

(v) puis installez les packages requirements du projet à l'aide de la commande:
pip install -r requirements.txt


## Comment utiliser l'Appli:

### Experience utilisateur:

(i) avec votre terminal, positionnez vous dans le dossier dans lequel vous avez installé l'Appli

(ii) activez l'environnement virtuel

(iii) ensuite tapez la commande 
$ python3 manage.py runserver

pour exécuter le serveur de développement

### Experience administrateur:


