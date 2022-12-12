// Github: https://github.com/alchemyplatform/alchemy-sdk-js
// Setup: npm install alchemy-sdk
const { Network, Alchemy } = require("alchemy-sdk");
_apiKey = "3VDBZXBKxInSgBVC4Ku6yIDSsObPdBob"
// Optional Config object, but defaults to demo api-key and eth-mainnet.
let tokenObject = {
    name: "",
    symbol: "",
    logo: "",
    tokenAddress: "",
    tokenBalance: ""
}

let nftObject = {
    title: "",
    contactAddress: "",
    tokenID: "",
    symbol: "",
    description: "",
    tokenImage: "",
    tokenType: "",

}
const getERC20TokensData = async (userAddress, evmNetwork) => {
    let returnAllTokenData = []

    const settings = {
        apiKey: _apiKey, // Replace with your Alchemy API Key.
        network: evmNetwork, // Replace with your network.
    };
    const alchemy = new Alchemy(settings);

    // Print token balances of USDC in Vitalik's address
    const results = await alchemy.core.getTokenBalances(userAddress)
    console.log(results)

    for (let i = 0; i < results.tokenBalances.length; i++) {
        alchemy.core.getTokenMetadata(results.tokenBalances[i].contractAddress).then(
            (response) => {
                console.log(response)
                let balanceInt = parseInt(results.tokenBalances[i].tokenBalance);
                tokenObject.name = response.name;
                tokenObject.symbol = response.symbol;
                tokenObject.logo = response.logo;
                tokenObject.tokenBalance = balanceInt / 10 ** (response.decimals);
                tokenObject.tokenAddress = results.tokenBalances[i].contractAddress;
                //console.log("TokenObj", tokenObject);

                returnAllTokenData.push(tokenObject);

                tokenObject = {
                    name: "",
                    symbol: "",
                    logo: "",
                    tokenAddress,
                    tokenBalance: ""
                }
                //console.log(returnAllTokenData)

            }
        );
    }
    return returnAllTokenData;
}

const userAddress = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045";
const evmNetwork = Network.ETH_MAINNET

//getERC20TokensData(userAddress, evmNetwork)


const getNFTdata = async (userAddress, evmNetwork) => {
    let returnAllNFTData = []

    const settings = {
        apiKey: _apiKey, // Replace with your Alchemy API Key.
        network: evmNetwork, // Replace with your network.
    };
    const alchemy = new Alchemy(settings);

    alchemy.nft.getNftsForOwner(userAddress).then(
        (response) => {
            response.ownedNfts.forEach((element) => {
                console.log(element)
                nftObject.contactAddress = element.contract.address
                nftObject.tokenImage = element.media[0].gateway
                nftObject.title = element.contract.name
                nftObject.symbol = element.contract.symbol
                nftObject.tokenType = element.contract.tokenType
                nftObject.description = element.description
                nftObject.tokenID = element.tokenId
                console.log(nftObject)
                returnAllNFTData.push(nftObject);

                nftObject = {
                    title: "",
                    contactAddress: "",
                    tokenID: "",
                    symbol: "",
                    description: "",
                    tokenImage: "",
                    tokenType: "",

                }

            });

        }
    )
    return returnAllNFTData;

}

getNFTdata(userAddress, evmNetwork)