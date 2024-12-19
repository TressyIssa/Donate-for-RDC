# Plateforme de Don basé sur la Blockchain | Pour l'aide aux sinistré de la RDC
![issa](https://github.com/user-attachments/assets/ef1b1a44-6e6f-465e-9f8a-ffe99278fdfa)

## Introduction
This project addresses the challenges of transparency and traceability in the management of donation funds in the Democratic Republic of Congo (DRC). Based on blockchain technology, this platform ensures secure, transparent and real-time monitoring of donations, thus increasing donor confidence by reducing transaction costs.

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
## Pre-requisite:
- **Install NodeJS in your machine:** https://nodejs.org/en/download
- **Install VScode in your machine:** https://code.visualstudio.com/download

## Installing a cryptocurrency wallet:
To utilize the benefits of blockchain first of all we need a cryptocurrency wallet, there are many available in the market such as MetaMask, Coinbase, BitPay, etc.

For this project we will install one of the most popular among them i.e. MetaMask

The steps are as follows:

- **1. Create a new wallet**
- 
  ![met](https://github.com/user-attachments/assets/7e176a40-b9c0-4d57-98a0-ba6c690eb1cd)

- **2.Here we have our crypto wallet**
  
  ![metamaskjpg](https://github.com/user-attachments/assets/e885edc0-bab5-4c4d-8f89-42bdcb1bad46)
  
But as you may notice, we have no funds here 😔, and buying Ethereum could be quite expensive, so what can do we do ?

Let's install a local blockchain where we can test all our stuff.

## Installing Ganache:

1. Visit Truffle Suite to download Ganache

   ![ganac](https://github.com/user-attachments/assets/d02243dd-4fbf-4b06-a478-86c37bbf89d8)
   
2. Here we have it, our own local blockchain
   ![ganache-3](https://github.com/user-attachments/assets/3bd28bdd-d8d8-45e3-af8b-5fa4842c4f5d)
So as of now we have our Crypto wallet set up done, and our Local Blockchain setup done; but how do we connect these two ?

## Connecting Ganache account to MetaMask Wallet:

1. Click on the MetaMask extension and click add new network
   ![metamask-g](https://github.com/user-attachments/assets/2530c110-a4d8-4b84-899a-1ac0bdfd3a2f)
   
2. Add the following details, like this
   ![metamask-ganache-jpg](https://github.com/user-attachments/assets/2ac5053f-ab00-43b1-865b-50fbc8ec1aed)
   
3. And we are done with connecting our local blockchain to metamask wallet
   ![ganache-6](https://github.com/user-attachments/assets/486097b8-9167-40f8-a4b0-0ea86bb2f24b)
   
4. Let's add an account from our chain to the metamask, so we can have the funds available, Copy the private key from here.
   ![key](https://github.com/user-attachments/assets/8a1b3ba7-fea3-42e4-be8d-1ba7d6c5c97f)
   
5. Click Import Account in MetaMask extension
![key2](https://github.com/user-attachments/assets/7cbc88c8-95e4-43c3-9324-902d12870d48)

6. and we have our funds in our wallet (locally only though)
   ![ether](https://github.com/user-attachments/assets/8d8c2705-f165-4570-b701-502a84c3b818)

# Plateforme de Don basé sur la Blockchain| FrontEnd
For our app interface, we will be using HTML, CSS, and JavaScript. This helps make the app simple to create and easier for everyone to follow.
You can create the frontend on your own or you can do the following.

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

- **1. Test dans la plateforme**: connexion d'un Utilisateur
  ![connexion](https://github.com/user-attachments/assets/c7d26d5d-ca49-40b4-8ea6-dbbe0d76d9d0)
  
- **2. Connexion**: L’utilisateur issafiti02@gmail.com vient de se connecter dans la plateforme. Il va maintenant passer
une transaction à l’aide de son portefeuille électronique MetaMask.

  ![WhatsApp Image 2024-12-10 at 19 54 16](https://github.com/user-attachments/assets/c5687b44-efb7-452a-9d13-124bbf8a38d5)
  
- **3. Déclenchement de l'evenement de transation sur MetaMask grâce à Web3**
![WhatsApp Image 2024-12-10 at 19 54 15](https://github.com/user-attachments/assets/7cbfa4cb-e384-4f36-b78a-59d06460db3b)

- **Nous voyons la présence du hash de la Transaction**
  ![WhatsApp Image 2024-12-10 at 19 54 16 (1)](https://github.com/user-attachments/assets/9a9206fe-471a-49bd-9f2b-3e058535bb4c)
  
- **Registre distribuer**
  ![WhatsApp Image 2024-12-10 at 20 49 07](https://github.com/user-attachments/assets/53b92eff-5b81-4e7f-b6ff-e72c7f9b33c6)

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
For inquiries, please contact [issafiti02@gmail.com].




