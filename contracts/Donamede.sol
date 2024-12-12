// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

contract DonationContract {
    address public owner;

    event DonationReceived(address indexed donor, uint amount);
    event FundsWithdrawn(uint amount);

    constructor() {
        owner = msg.sender;
    }

    function donate() external payable {
        require(msg.value > 0, "Donation must be greater than 0");
        emit DonationReceived(msg.sender, msg.value);
    }

    function withdraw(uint amount) external {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        require(amount <= address(this).balance, "Insufficient balance in contract");
        payable(owner).transfer(amount);
        emit FundsWithdrawn(amount);
    }

    function getBalance() external view returns (uint) {
        return address(this).balance;
    }
}
