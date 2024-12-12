// Importation de Web3
import Web3 from 'web3';

let web3;

// Fonction asynchrone pour se connecter à MetaMask
async function connectMetaMask() {
    if (window.ethereum) {
        web3 = new Web3(window.ethereum);
        try {
            // Demande d'autorisation de connexion à MetaMask
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connecté à MetaMask');
        } catch (error) {
            console.error("L'utilisateur a refusé l'accès à MetaMask");
        }
    } else if (window.web3) {
        // Si MetaMask injecte déjà Web3
        web3 = new Web3(window.web3.currentProvider);
        console.log("Web3 trouvé via MetaMask");
    } else {
        console.log("Veuillez installer MetaMask !");
    }
}

// Appel de la fonction pour tenter la connexion à MetaMask au chargement du script
connectMetaMask();

// Exemple de fonction pour envoyer une transaction depuis l'application
async function sendTransaction(toAddress, amountInEther) {
    if (!web3) {
        console.log("MetaMask n'est pas connecté !");
        return;
    }

    // Conversion du montant en Wei
    const amountInWei = Web3.utils.toWei(amountInEther, 'ether');
    
    const accounts = await web3.eth.getAccounts();
    const fromAddress = accounts[0];

    // Configuration de la transaction
    const transactionParameters = {
        to: toAddress,
        from: fromAddress,
        value: amountInWei,
        gas: '2000000'
    };

    // Envoi de la transaction via MetaMask
    try {
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log(`Transaction envoyée avec succès ! Hash de transaction : ${txHash}`);
    } catch (error) {
        console.error("Erreur lors de l'envoi de la transaction :", error);
    }
}

// Associez la fonction sendTransaction à l'événement click du bouton
document.addEventListener('DOMContentLoaded', () => {
    const donateButton = document.getElementById('donateButton');
    if (donateButton) {
        donateButton.addEventListener('click', () => {
            const toAddress = '0x518Ef87c7d4A4BB1D4B5Af215b560c9Ccd74F79d';  // Adresse de destination
            const amountInEther = '0.1';  // Montant en ETH (ou adapter selon l'entrée utilisateur)
            sendTransaction(toAddress, amountInEther);
        });
    }
});
