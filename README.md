# Blockchain Donation Platform

## Introduction
This project addresses the challenges of transparency and traceability in managing donation funds in the Democratic Republic of Congo (DRC). Leveraging blockchain technology, this platform ensures secure, transparent, and real-time tracking of donations, thereby increasing donor confidence and reducing administrative costs.

## Features
- **Blockchain Technology**: Built on the Ethereum blockchain to provide an immutable and transparent record of all transactions.
- **Smart Contracts**: Developed in Solidity to automate the management and distribution of funds.
- **Real-Time Tracking**: Donors can monitor the usage of their contributions in real-time.
- **Secure Transactions**: Integration with MetaMask ensures secure interactions with the blockchain.
- **Local Testing**: Utilizes Ganache for a robust local development environment.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django Framework
- **Blockchain**: Ethereum, Solidity
- **Tools**: MetaMask, Ganache, Web3.js

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/blockchain-donation-platform.git
   ```
2. Navigate to the project directory:
   ```bash
   cd blockchain-donation-platform
   ```
3. Install dependencies:
   - For Django backend:
     ```bash
     pip install -r requirements.txt
     ```
   - For frontend:
     Ensure you have a modern browser that supports MetaMask.

4. Set up the Ethereum local environment:
   - Install Ganache and configure it to simulate a blockchain network.
   - Deploy the smart contract using Remix or Truffle.

5. Run the Django server:
   ```bash
   python manage.py runserver
   ```
6. Access the application:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage
- **Donor Registration**: Sign up and log in to make a donation.
- **Project Listing**: View available projects and their details.
- **Donation**: Make secure donations with real-time blockchain verification.
- **Transaction Monitoring**: Track donation history and project updates.

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For inquiries, please contact [your-email@example.com].


..................................................................................................
# Plateforme de Don basé sur la Blockchain | Destiné aux sinistré de la RDC .



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




