const DonationContract = artifacts.require("DonationContract");

module.exports = async function (deployer) {
    await deployer.deploy(DonationContract); // Supprimez { gas: 9000000 }
};
