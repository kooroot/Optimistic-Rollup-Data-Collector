import pandas as pd
import requests

#Before running this code, you need to get your own API key from Alchemy.
url = "https://opt-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
df = pd.DataFrame()

with open('OPblock.csv', 'w+') as f:
    for i in range(1, 216001):
        try:
            payload = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "eth_getBlockByNumber",
                "params": [hex(i), True]
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)

            #temp_df = pd.DataFrame(response.json()['result']['transactions'])[['blockHash', 'blockNumber', 'hash', 'gas', 'gasPrice', 'l1BlockNumber', 'l1Timestamp']]
            temp_df = pd.DataFrame(response.json()['result']['transactions'])[['blockHash', 'blockNumber', 'hash', 'gas', 'gasPrice']]
            df = df._append(temp_df, ignore_index=True)
            print(str(i)+"th block success.")
        except:
            print(str(i)+"th block failed.")
            pass
    df.to_csv(f, index=False)
    print("File saved.")

