// Vérifiez si MetaMask est disponible
if (typeof window.ethereum !== 'undefined') {
    // Créez une instance Web3 en utilisant le provider MetaMask
    var web3 = new Web3(window.ethereum);
    console.log("MetaMask est installé et Web3 est chargé.");
} else {
    alert("MetaMask n'est pas installé ! Veuillez l'installer pour continuer.");
}

async function sendTransaction() {
    // Vérifiez que MetaMask est connecté
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Demandez l'accès aux comptes de MetaMask
            await ethereum.request({ method: 'eth_requestAccounts' });
            
            // Récupérez le compte de l'utilisateur connecté
            const accounts = await web3.eth.getAccounts();
            const sender = accounts[0];

            // Récupérez l'adresse du destinataire et le montant du formulaire
            const recipient = document.getElementById('recipient').value;
            const amount = document.getElementById('amount').value;

            // Convertissez le montant en Wei
            const valueInWei = web3.utils.toWei(amount, 'ether');

            // Envoyez la transaction
            web3.eth.sendTransaction({
                from: sender,
                to: recipient,
                value: valueInWei,
                gas: 21000  // Limite de gaz pour un transfert simple d'ETH
            })
            .on('transactionHash', function(hash) {
                document.getElementById('status').innerText = `Transaction envoyée avec succès ! Hash : ${hash}`;
                console.log(`Transaction envoyée avec succès ! Hash : ${hash}`);
            })
            .on('error', function(error) {
                document.getElementById('status').innerText = `Erreur lors de l'envoi : ${error.message}`;
                console.error(error);
            });

        } catch (error) {
            document.getElementById('status').innerText = `Erreur : ${error.message}`;
            console.error(error);
        }
    } else {
        alert("MetaMask n'est pas installé !");
    }
}
