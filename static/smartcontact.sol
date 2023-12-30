// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

contract CandySupplyChain {
    struct User {
        string userID;
        string userName;
        string userEmail;
        string userLg;
        string userPass;
        string role;
    }

    struct Trans {
        string transID;
        string transTime;
        string transHash;
        string userID;
        string productID;
    }

    struct Product {
        string proID;
        string proName;
        string manufacturerAdd;
        string manufacturerName;
        string manufacturerCont;
        string distributorAdd;
        string distributorName;
        string distributorCont;
        string otherDetails;
    }

    mapping(string => User) public users;
    mapping(string => Trans) public transactions;
    mapping(string => Product) public products;

    function addUser(
        string memory _userID,
        string memory _userName,
        string memory _userEmail,
        string memory _userLg,
        string memory _userPass,
        string memory _role
    ) public {
        User storage newUser = users[_userID];
        newUser.userID = _userID;
        newUser.userName = _userName;
        newUser.userEmail = _userEmail;
        newUser.userLg = _userLg;
        newUser.userPass = _userPass;
        newUser.role = _role;
    }

    function addTransaction(
        string memory _transID,
        string memory _transTime,
        string memory _transHash,
        string memory _userID,
        string memory _productID
    ) public {
        Trans storage newTransaction = transactions[_transID];
        newTransaction.transID = _transID;
        newTransaction.transTime = _transTime;
        newTransaction.transHash = _transHash;
        newTransaction.userID = _userID;
        newTransaction.productID = _productID;
    }

    function addProduct(
        string memory _proID,
        string memory _proName,
        string memory _manufacturerAdd,
        string memory _manufacturerName,
        string memory _manufacturerCont,
        string memory _distributorAdd,
        string memory _distributorName,
        string memory _distributorCont,
        string memory _otherDetails
    ) public {
        Product storage newProduct = products[_proID];
        newProduct.proID = _proID;
        newProduct.proName = _proName;
        newProduct.manufacturerAdd = _manufacturerAdd;
        newProduct.manufacturerName = _manufacturerName;
        newProduct.manufacturerCont = _manufacturerCont;
        newProduct.distributorAdd = _distributorAdd;
        newProduct.distributorName = _distributorName;
        newProduct.distributorCont = _distributorCont;
        newProduct.otherDetails = _otherDetails;
    }

    function getUser(string memory _userID) public view returns (User memory) {
        return users[_userID];
    }

    function getTransaction(string memory _transID) public view returns (Trans memory) {
        return transactions[_transID];
    }

    function getProduct(string memory _proID) public view returns (Product memory) {
        return products[_proID];
    }
    function hashData(
        string memory user_id,
        string memory product_id,
        string memory trans_id,
        string memory time
    ) public pure returns (string memory) {
        // Gộp dữ liệu lại thành một chuỗi
        string memory concatenatedData = string(abi.encodePacked(user_id, product_id, trans_id, time));
        bytes32 hashedData = sha256(bytes(concatenatedData));

        return toString(hashedData);
    }

    function toString(bytes32 value) internal pure returns (string memory) {
        bytes memory strBytes = new bytes(64);
        for (uint i = 0; i < 32; i++) {
            bytes1 currentByte = bytes1(uint8(uint(value) / (2**(8*(31 - i)))));
            bytes1 highNibble = bytes1(uint8(currentByte) / 16);
            bytes1 lowNibble = bytes1(uint8(currentByte) - 16 * uint8(highNibble));
            strBytes[2*i] = char(highNibble);
            strBytes[2*i + 1] = char(lowNibble);
        }
        return string(strBytes);
    }

    // Hàm chuyển đổi bytes1 sang char (dùng trong trường hợp sha256)
    function char(bytes1 b) internal pure returns (bytes1 c) {
        if (uint8(b) < 10) return bytes1(uint8(b) + 0x30);
        else return bytes1(uint8(b) + 0x57);
    }
}