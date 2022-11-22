const { AccountLayout, TOKEN_PROGRAM_ID } = require("@solana/spl-token");
const { clusterApiUrl, Connection, PublicKey } = require("@solana/web3.js");
const axios = require("axios")
userAddress = "L6AxKPADzg29Kbkit13v3pzMi7LSam5W5ANqP4VJXzp"
userAddress2 = "3PaXGhty44YzmDDCDHKe5UJksAX2U9tb2Y6FzQyihxNp"


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

const getUserSolTokenData = async (userAddress) => {
    let returnAllTokenData = []
    let accountData = await axios.get(`https://public-api.solscan.io/account/tokens?account=${userAddress}`)
    accountData.data.forEach((element) => {

        tokenObject.name = element.tokenName,
            tokenObject.symbol = element.tokenSymbol,
            tokenObject.logo = element.tokenIcon,
            tokenObject.tokenAddress = element.tokenAddress,
            tokenObject.tokenBalance = element.tokenAmount.amount / element.tokenAmount.decimals
        console.log(tokenObject)
        returnAllTokenData.push(tokenObject);

        tokenObject = {
            name: "",
            symbol: "",
            logo: "",
            tokenAddress: "",
            tokenBalance: ""
        }
    });
    return returnAllTokenData;
};

//getUserSolTokenData(userAddress)

const getUserSolNFTdata = async (userAddress) => {
    let returnAllNFTData = []
    var options = {
        method: 'GET',
        url: `https://api.nftport.xyz/v0/solana/accounts/${userAddress}`,
        headers: {
            'Content-Type': 'application/json',
            Authorization: 'd070c4b4-c972-4b32-9ee8-96439e6cdf72'
        }
    };

    axios.request(options).then(function async(response) {
        //console.log(response.data.nfts);
        response.data.nfts.forEach((element) => {
            nftObject.contactAddress = element.mint_address;
            try {
                await axios.get(element.metadata_url).then(async (result) => {
                    // nftObject.contactAddress = element.mint_address;
                    // nftObject.contactAddress = element.mint_address;
                    // nftObject.contactAddress = element.mint_address;
                    // nftObject.contactAddress = element.mint_address;
                    // nftObject.contactAddress = element.mint_address;
                    // nftObject.contactAddress = element.mint_address;

                    console.log(result.data)
                });
            } catch (e) {

            }
        })

    }).catch(function (error) {
        //console.error(error);
    });
    return returnAllNFTData
}

getUserSolNFTdata(userAddress2)
/*
Token                                         Balance
------------------------------------------------------------
7e2X5oeAAJyUTi4PfSGXFLGhyPw2H8oELm1mx87ZCgwF  84
AQoKYV7tYpTrFZN6P5oUufbQKAUr9mNYGe1TTJC9wajM  100
AQoKYV7tYpTrFZN6P5oUufbQKAUr9mNYGe1TTJC9wajM  0
AQoKYV7tYpTrFZN6P5oUufbQKAUr9mNYGe1TTJC9wajM  1
*/