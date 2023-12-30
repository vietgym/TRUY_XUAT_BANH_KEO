let web3;

// const contractAddress = '0xd9145CCE52D386f254917e481eB44e9943F39138';
// const contractAbi = [
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "_proID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_proName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_manufacturerAdd",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_manufacturerName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_manufacturerCont",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_distributorAdd",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_distributorName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_distributorCont",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_otherDetails",
// 				"type": "string"
// 			}
// 		],
// 		"name": "addProduct",
// 		"outputs": [],
// 		"stateMutability": "nonpayable",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "_transID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_transTime",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_transHash",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_userID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_productID",
// 				"type": "string"
// 			}
// 		],
// 		"name": "addTransaction",
// 		"outputs": [],
// 		"stateMutability": "nonpayable",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "_userID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_userName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_userEmail",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_userLg",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_userPass",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "_role",
// 				"type": "string"
// 			}
// 		],
// 		"name": "addUser",
// 		"outputs": [],
// 		"stateMutability": "nonpayable",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "_proID",
// 				"type": "string"
// 			}
// 		],
// 		"name": "getProduct",
// 		"outputs": [
// 			{
// 				"components": [
// 					{
// 						"internalType": "string",
// 						"name": "proID",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "proName",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "manufacturerAdd",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "manufacturerName",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "manufacturerCont",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "distributorAdd",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "distributorName",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "distributorCont",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "otherDetails",
// 						"type": "string"
// 					}
// 				],
// 				"internalType": "struct CandySupplyChain.Product",
// 				"name": "",
// 				"type": "tuple"
// 			}
// 		],
// 		"stateMutability": "view",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "_transID",
// 				"type": "string"
// 			}
// 		],
// 		"name": "getTransaction",
// 		"outputs": [
// 			{
// 				"components": [
// 					{
// 						"internalType": "string",
// 						"name": "transID",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "transTime",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "transHash",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "userID",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "productID",
// 						"type": "string"
// 					}
// 				],
// 				"internalType": "struct CandySupplyChain.Trans",
// 				"name": "",
// 				"type": "tuple"
// 			}
// 		],
// 		"stateMutability": "view",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "_userID",
// 				"type": "string"
// 			}
// 		],
// 		"name": "getUser",
// 		"outputs": [
// 			{
// 				"components": [
// 					{
// 						"internalType": "string",
// 						"name": "userID",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "userName",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "userEmail",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "userLg",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "userPass",
// 						"type": "string"
// 					},
// 					{
// 						"internalType": "string",
// 						"name": "role",
// 						"type": "string"
// 					}
// 				],
// 				"internalType": "struct CandySupplyChain.User",
// 				"name": "",
// 				"type": "tuple"
// 			}
// 		],
// 		"stateMutability": "view",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "user_id",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "product_id",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "trans_id",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "time",
// 				"type": "string"
// 			}
// 		],
// 		"name": "hashData",
// 		"outputs": [
// 			{
// 				"internalType": "string",
// 				"name": "",
// 				"type": "string"
// 			}
// 		],
// 		"stateMutability": "pure",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "",
// 				"type": "string"
// 			}
// 		],
// 		"name": "products",
// 		"outputs": [
// 			{
// 				"internalType": "string",
// 				"name": "proID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "proName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "manufacturerAdd",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "manufacturerName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "manufacturerCont",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "distributorAdd",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "distributorName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "distributorCont",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "otherDetails",
// 				"type": "string"
// 			}
// 		],
// 		"stateMutability": "view",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "",
// 				"type": "string"
// 			}
// 		],
// 		"name": "transactions",
// 		"outputs": [
// 			{
// 				"internalType": "string",
// 				"name": "transID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "transTime",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "transHash",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "userID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "productID",
// 				"type": "string"
// 			}
// 		],
// 		"stateMutability": "view",
// 		"type": "function"
// 	},
// 	{
// 		"inputs": [
// 			{
// 				"internalType": "string",
// 				"name": "",
// 				"type": "string"
// 			}
// 		],
// 		"name": "users",
// 		"outputs": [
// 			{
// 				"internalType": "string",
// 				"name": "userID",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "userName",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "userEmail",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "userLg",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "userPass",
// 				"type": "string"
// 			},
// 			{
// 				"internalType": "string",
// 				"name": "role",
// 				"type": "string"
// 			}
// 		],
// 		"stateMutability": "view",
// 		"type": "function"
// 	}
// ]
// const contract = new web3.eth.Contract(contractAbi, contractAddress);
// alert(contract);
async function connectToMetaMask() {
    if (window.ethereum) {
        try {
            await window.ethereum.request({method: 'eth_requestAccounts'});
            web3 = new Web3(window.ethereum);
            const accounts = await web3.eth.getAccounts();
            alert('Connected to MetaMask! Current account: ' + accounts[0]);
        } catch (error) {
            alert('Connection to MetaMask failed: ' + error.message);
        }
    } else {
        alert('Please install MetaMask to use this feature');
    }
}

async function checkEtherBalance() {
    if (!web3) {
        alert('Please connect to MetaMask first');
        return;
    }

    const accounts = await web3.eth.getAccounts();
    const balanceWei = await web3.eth.getBalance(accounts[0]);
    const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

    // Assuming an exchange rate of 1 ETH = 1000 USD (replace with the actual exchange rate)
    const exchangeRate = 1000;
    const balanceUSD = balanceEther * exchangeRate;

    alert(`Ether Balance: ${balanceEther} ETH\nEquivalent in USD: $${balanceUSD}`);
}

// async function print(){
// 	const contractAddress = '0xd9145CCE52D386f254917e481eB44e9943F39138';
// 	const contractAbi = [
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "_proID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_proName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_manufacturerAdd",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_manufacturerName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_manufacturerCont",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_distributorAdd",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_distributorName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_distributorCont",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_otherDetails",
// 					"type": "string"
// 				}
// 			],
// 			"name": "addProduct",
// 			"outputs": [],
// 			"stateMutability": "nonpayable",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "_transID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_transTime",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_transHash",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_userID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_productID",
// 					"type": "string"
// 				}
// 			],
// 			"name": "addTransaction",
// 			"outputs": [],
// 			"stateMutability": "nonpayable",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "_userID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_userName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_userEmail",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_userLg",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_userPass",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "_role",
// 					"type": "string"
// 				}
// 			],
// 			"name": "addUser",
// 			"outputs": [],
// 			"stateMutability": "nonpayable",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "_proID",
// 					"type": "string"
// 				}
// 			],
// 			"name": "getProduct",
// 			"outputs": [
// 				{
// 					"components": [
// 						{
// 							"internalType": "string",
// 							"name": "proID",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "proName",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "manufacturerAdd",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "manufacturerName",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "manufacturerCont",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "distributorAdd",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "distributorName",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "distributorCont",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "otherDetails",
// 							"type": "string"
// 						}
// 					],
// 					"internalType": "struct CandySupplyChain.Product",
// 					"name": "",
// 					"type": "tuple"
// 				}
// 			],
// 			"stateMutability": "view",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "_transID",
// 					"type": "string"
// 				}
// 			],
// 			"name": "getTransaction",
// 			"outputs": [
// 				{
// 					"components": [
// 						{
// 							"internalType": "string",
// 							"name": "transID",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "transTime",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "transHash",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "userID",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "productID",
// 							"type": "string"
// 						}
// 					],
// 					"internalType": "struct CandySupplyChain.Trans",
// 					"name": "",
// 					"type": "tuple"
// 				}
// 			],
// 			"stateMutability": "view",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "_userID",
// 					"type": "string"
// 				}
// 			],
// 			"name": "getUser",
// 			"outputs": [
// 				{
// 					"components": [
// 						{
// 							"internalType": "string",
// 							"name": "userID",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "userName",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "userEmail",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "userLg",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "userPass",
// 							"type": "string"
// 						},
// 						{
// 							"internalType": "string",
// 							"name": "role",
// 							"type": "string"
// 						}
// 					],
// 					"internalType": "struct CandySupplyChain.User",
// 					"name": "",
// 					"type": "tuple"
// 				}
// 			],
// 			"stateMutability": "view",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "user_id",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "product_id",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "trans_id",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "time",
// 					"type": "string"
// 				}
// 			],
// 			"name": "hashData",
// 			"outputs": [
// 				{
// 					"internalType": "string",
// 					"name": "",
// 					"type": "string"
// 				}
// 			],
// 			"stateMutability": "pure",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "",
// 					"type": "string"
// 				}
// 			],
// 			"name": "products",
// 			"outputs": [
// 				{
// 					"internalType": "string",
// 					"name": "proID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "proName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "manufacturerAdd",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "manufacturerName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "manufacturerCont",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "distributorAdd",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "distributorName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "distributorCont",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "otherDetails",
// 					"type": "string"
// 				}
// 			],
// 			"stateMutability": "view",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "",
// 					"type": "string"
// 				}
// 			],
// 			"name": "transactions",
// 			"outputs": [
// 				{
// 					"internalType": "string",
// 					"name": "transID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "transTime",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "transHash",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "userID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "productID",
// 					"type": "string"
// 				}
// 			],
// 			"stateMutability": "view",
// 			"type": "function"
// 		},
// 		{
// 			"inputs": [
// 				{
// 					"internalType": "string",
// 					"name": "",
// 					"type": "string"
// 				}
// 			],
// 			"name": "users",
// 			"outputs": [
// 				{
// 					"internalType": "string",
// 					"name": "userID",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "userName",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "userEmail",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "userLg",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "userPass",
// 					"type": "string"
// 				},
// 				{
// 					"internalType": "string",
// 					"name": "role",
// 					"type": "string"
// 				}
// 			],
// 			"stateMutability": "view",
// 			"type": "function"
// 		}
// 	]
// 	const contract = new web3.eth.Contract(contractAbi, contractAddress);
// 	console.log(contract);
// }

async function makeHashTrans(user_id, product_id, trans_id, time) {
	const contractAddress = '0xd9145CCE52D386f254917e481eB44e9943F39138';
	const contractAbi = [
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_proID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_proName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_manufacturerAdd",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_manufacturerName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_manufacturerCont",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_distributorAdd",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_distributorName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_distributorCont",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_otherDetails",
					"type": "string"
				}
			],
			"name": "addProduct",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_transID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_transTime",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_transHash",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_userID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_productID",
					"type": "string"
				}
			],
			"name": "addTransaction",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_userID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_userName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_userEmail",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_userLg",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_userPass",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_role",
					"type": "string"
				}
			],
			"name": "addUser",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_proID",
					"type": "string"
				}
			],
			"name": "getProduct",
			"outputs": [
				{
					"components": [
						{
							"internalType": "string",
							"name": "proID",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "proName",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "manufacturerAdd",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "manufacturerName",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "manufacturerCont",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "distributorAdd",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "distributorName",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "distributorCont",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "otherDetails",
							"type": "string"
						}
					],
					"internalType": "struct CandySupplyChain.Product",
					"name": "",
					"type": "tuple"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_transID",
					"type": "string"
				}
			],
			"name": "getTransaction",
			"outputs": [
				{
					"components": [
						{
							"internalType": "string",
							"name": "transID",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "transTime",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "transHash",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "userID",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "productID",
							"type": "string"
						}
					],
					"internalType": "struct CandySupplyChain.Trans",
					"name": "",
					"type": "tuple"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_userID",
					"type": "string"
				}
			],
			"name": "getUser",
			"outputs": [
				{
					"components": [
						{
							"internalType": "string",
							"name": "userID",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "userName",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "userEmail",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "userLg",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "userPass",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "role",
							"type": "string"
						}
					],
					"internalType": "struct CandySupplyChain.User",
					"name": "",
					"type": "tuple"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "user_id",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "product_id",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "trans_id",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "time",
					"type": "string"
				}
			],
			"name": "hashData",
			"outputs": [
				{
					"internalType": "string",
					"name": "",
					"type": "string"
				}
			],
			"stateMutability": "pure",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "",
					"type": "string"
				}
			],
			"name": "products",
			"outputs": [
				{
					"internalType": "string",
					"name": "proID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "proName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "manufacturerAdd",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "manufacturerName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "manufacturerCont",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "distributorAdd",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "distributorName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "distributorCont",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "otherDetails",
					"type": "string"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "",
					"type": "string"
				}
			],
			"name": "transactions",
			"outputs": [
				{
					"internalType": "string",
					"name": "transID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "transTime",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "transHash",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "userID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "productID",
					"type": "string"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "",
					"type": "string"
				}
			],
			"name": "users",
			"outputs": [
				{
					"internalType": "string",
					"name": "userID",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "userName",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "userEmail",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "userLg",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "userPass",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "role",
					"type": "string"
				}
			],
			"stateMutability": "view",
			"type": "function"
		}
	]
	const contract = new web3.eth.Contract(contractAbi, contractAddress);
	console.log(contract);
    try {
        const accounts = await web3.eth.getAccounts();
		const result = await contract.methods.hashData(user_id, product_id, trans_id, time).send({ from: accounts[0] });

        console.log('Hash result:', result);
		alert(result);
    } catch (error) {
        console.error('Error calling hashData:', error);
    }
}