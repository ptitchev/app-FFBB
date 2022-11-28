# **Projet : app ffbb**

## **Description**

Ce projet est une application web permettant d'afficher sur une carte les matchs de basketball près de chez sois. Pour ce faire, il scrape l'ensemble des championnats présents dans le site de la [ffbb](http://www.ffbb.com/). Nous stockons ensuite les données dans une base de données postegreSQL. Le backend est réalisé en python avec fastAPI et le frontend est réalisé avec React Js.

Ce projet est réalisé dans le cadre scolaire. 

<br>

## **User Guide**

### **Récupération du projet**

Tout d'abord verifiez que vous avez bien installé [Git](https://git-scm.com/) sur votre espace de travail afin de récupérer les fichiers.
Ensuite, clonez le dossier dans le répertoire souhaité en utilisant la commande [git clone](https://github.com/ptitchev/app-FFBB.git) afin d'avoir accès au répertoire.

```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > git clone https://github.com/ptitchev/app-FFBB.git
$:~/<WORKDIR> > cd app-FFBB/
```

<br>

### **Lancement du projet**

Avant de faire les manipulations suivantes, il faut s'assurer que [docker](https://docs.docker.com/get-docker/) soit bien installé. 
Ensuite, mettez vous dans le bon répertoire et lancez la commande `docker-compose up`. Cette commande va lancer l'environnement.
```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > cd app-FFBB/
$:~/app-FFBB > docker-compose up
```
<br>

### **Fonctionnement du dashboard**

L'application web est composé d'une barre de recherche où nous pouvons entrer une localisation et une date. En appuyant sur search, la map affichera les matchs présents autours de la localisation.

<br>

### **Liste des technologies utilisés**

* *React Js*.
* *FastApi*.
* *Docker*.
* *Tailwind Css*.
* *Request*.

 
<br>

*<div style="text-align: right"> Jules Chevenet - Axel Cochet </div>*

