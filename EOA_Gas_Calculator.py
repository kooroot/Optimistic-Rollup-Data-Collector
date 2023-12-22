import requests

def get_total_gas_used(etherscan_api_key, account_address):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": account_address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 2000,
        "offset": 50,
        "sort": "desc",
        "apikey": etherscan_api_key
    }

    response = requests.get(url, params=params)
    transactions = response.json()["result"]
    #print(transactions)

    total_gas_used = sum(int(tx["gasUsed"]) for tx in transactions if tx["from"].lower() == account_address.lower())
    #total_gas_used = int(transactions[-1]['cumulativeGasUsed'])

    return total_gas_used

# Etherscan API 키와 계정 주소
etherscan_api_key = "YOUR_ETHERSCAN_API_KEY" 
account_address = "YOUR_ACCOUNT_ADDRESS"

total_gas = get_total_gas_used(etherscan_api_key, account_address)
print(f"Account {account_address} has used a total of {total_gas} gas.")
