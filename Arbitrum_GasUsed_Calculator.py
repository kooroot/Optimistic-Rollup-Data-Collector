from web3 import Web3

# 아비트럼 네트워크와 연결
w3 = Web3(Web3.HTTPProvider('YOUR_API_KEY'))

def get_transactions_and_calculate_gas(start_block, end_block):
    total_gas_used = 0

    # 주어진 범위의 블록들에 대해 반복
    for block_number in range(start_block, end_block + 1):
        block = w3.eth.get_block(block_number, full_transactions=True)
        transactions = block['transactions']

        # 각 트랜잭션에 대해 예상 가스 비용 계산
        for tx in transactions:
            # 트랜잭션 상세 정보를 가져옴
            try:
                tx_receipt = w3.eth.get_transaction_receipt(tx.hash)
                total_gas_used += tx_receipt.gasUsed
                #print("Block Number: ", tx_receipt.blockNumber)
                #print("Used Gas: ", tx_receipt.gasUsed)
            except Exception as e:
                print(f"가스 추정 실패: {e}. \nBlock Number: " + str(tx_receipt['blockNumber']))

    return total_gas_used

start_block = 162353927  # 시작 블록 번호
end_block = 162353928  # 끝 블록 번호
total_used_gas = get_transactions_and_calculate_gas(start_block, end_block)
print(f"총 사용 가스 비용: {total_used_gas} Gas")