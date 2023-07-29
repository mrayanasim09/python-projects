# This program is made by MRayan Asim
# Packages needed:
# pip install hashlib
import hashlib


def mine_block(previous_block_hash, transactions, difficulty):
    nonce = 0
    while True:
        block_data = str(nonce) + previous_block_hash + transactions
        block_hash = hashlib.sha256(block_data.encode()).hexdigest()

        if block_hash.startswith("0" * difficulty):
            return block_hash

        nonce += 1


# Example usage
previous_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
transactions = "Alice sends 1 BTC to Bob"
difficulty = 4

mined_block_hash = mine_block(previous_block_hash, transactions, difficulty)
print("Mined block hash:", mined_block_hash)
