# ChatBot de Suivi des Performances des connaissances scolaires avec LLM et RDF Cube.

Bienvenue dans notre projet qui combine des **Modèles de Langage de Grande Taille (LLM)** et des **Cubes RDF** pour offrir une solution innovante de suivi des performances éducatives. Ce projet permet de structurer des données éducatives et d'utiliser l'intelligence artificielle pour produire des analyses et des recommandations personnalisées en fonction des performances des étudiants.

## Contexte du Projet

Dans le cadre de l'éducation, il est essentiel de suivre et d'évaluer les performances des étudiants pour identifier les domaines où des améliorations sont nécessaires. Ce projet se concentre sur l'utilisation de **RDF Cube** pour structurer les données éducatives et de **LLM** pour générer des réponses aux questions posées en langage naturel par les utilisateurs (enseignants, administrateurs).

## Fonctionnalités Principales

- **Analyse des performances éducatives** : Basée sur différents critères tels que les cours, la classe, ou l'année.
- **Recommandations personnalisées** : Propose des actions ciblées pour améliorer les performances des étudiants ou des classes.
- **Interface utilisateur intuitive** : Les utilisateurs peuvent poser des questions en langage naturel pour obtenir des réponses sous forme de statistiques, tendances ou recommandations.

## Architecture du Système

L'application est constituée de trois principaux composants :

1. **Interface Utilisateur (UI)** : Permet aux utilisateurs de poser des questions et de visualiser les résultats.
2. **Module LLM** : Interprète les questions posées en langage naturel et génère des réponses pertinentes à partir des données RDF Cube.
3. **Cubes RDF** : Stocke et organise les données éducatives de manière multidimensionnelle, facilitant les requêtes complexes.

## Installation et Configuration

### Prérequis

- Python 3.10 ou plus récent
- **Poetry** pour la gestion des dépendances
- **Clé API OpenAI** pour interagir avec le modèle de langage

### Important : Clé OpenAI

Pour cloner et utiliser cette application, vous devez avoir une **clé API OpenAI** valide. Vous pouvez obtenir cette clé en créant un compte sur [OpenAI](https://openai.com/) et en générant une clé via leur interface de gestion des API. Cette clé sera nécessaire pour interagir avec les capacités du modèle de langage intégré à l'application.

### Étapes d'Installation

1. **Cloner le dépôt du projet :**

   ```bash
   https://github.com/Issasoro/ChatBot-RDFCube-LLM.git
   cd ChatBot-RDFCube-LLM
2. **Créer un environnement virtuel et l'activer :**
   ```bash.
   python -m venv .venv
   source .venv/bin/activate

3. **Créez un fichier .env et ajoutez-y votre clé API OpenAI**

   ```bash
   OPEN_API_KEY=votre_cle_api

4. **Lancer l'application dans Visual Studio Code :**
   Ouvrez le projet dans VSCode

   ```bash
   OPEN_API_KEY=votre_cle_api




