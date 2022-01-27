[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Projet WhatIsInMyPDF (Flask)

Ici, vous trouverez une application Flask qui vous permettra d'extraire le texte et les metadonées d'un pdf.

## Pré-requis

Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)

## Installation

### Avec Linux

#### Debian, Ubuntu

    $ sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev

#### Fedora, Red Hat

    $ sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel

#### macOS

    brew install pkg-config poppler python


### FLASK application

Créer un virtualenv et l'activer :

    $ python -m venv venv
    $ . venv/bin/activate

Installer WhatIsInMyPDF:

    $ pip install -r requirements.txt

Initialiser la base de donnees
    
    $ cd development/database
    $ python create_database.py
    $ cd ../..

# Run

## Avec Linux or Mac OS

    $ export FLASK_APP=development
    $ flask run

# Usage

Ouvrez http://localhost:5000 dans un navigateur pour essayer le logiciel ou utilisez l'API suivante.

## Les Packages utilisés:

### Utilisation de Pdfminer

Permet l'extraction du text et des metadonnées d'un fichier PDF.

### Utilisation de SQLLite

SQLite est une bibliothèque en langage C qui implémente un moteur de base de données SQL petit, rapide, autonome, très fiable et complet. SQLite est le moteur de base de données le plus utilisé au monde.

### Utilisation de Flask

Flask est une SDK qui permet, comme Django, de mettre en place une application.

## Specification API 

### Charger un fichier

Poster un fichier sur le serveur: 

**Requete**

    HTTP Methode: POST
    Route: /
    Alternate: /file
    # La méthode GET renvoie un formulaire de téléchargement HTML.
    # La méthode POST peut être utilisée pour télécharger un fichier PDF.

**Reponse**

    {
        "id": [id],
        "message": "[message]"}"
    }



### Verifier l'importation du fichier

Obtenez le statut d'un fichier téléchargé et afficher ses méta-données :

**Requete**

    HTTP Methode: GET
    Route: /file/{id}
    # Informations sur un document.
    # La méthode GET renvoie des métadonnées sur le document, spécifié par le paramètre ID.

**Reponse**

    {
        # ID of the uploaded PDF file, otherwise 'null' if not found (int)

        "author": "[author]",
        "subject": "[subject]", 
        "title": "[title]", 
        "number_of_pages": [number_of_pages], 
        "id": [id], 
        "status": "[status]"
    }

En cas de **error**, la réponse suivante est renvoyée :

    {
        "id": null,
        "message": "[message]"
    }

### Texte du fichier

Affichage du text d'un fichier.

**Requete**

    HTTP Methode: GET
    Route: /pdftext/{id}
    # Contenu d'un document en entrant l'id.
    # La méthode GET retourne le contenu d'un document.

**Reponse**

    {
        "content": [content]
    }

### Propreté du code

Avec Pylint:

    $ sudo apt install pylint
    $ export PYTHONPATH="venv/lib/python3.8/site-packages/"
    $ pylint --disable too-many-instance-attributes development/*

### Test du code avec pytest

    $ pytest
