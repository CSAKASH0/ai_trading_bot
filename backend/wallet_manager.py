from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"))

def get_balance(wallet):
    return w3.from_wei(w3.eth.get_balance(w3.to_checksum_address(wallet)), 'ether')

def send_transaction(data):
    sender = w3.to_checksum_address(data['from'])
    receiver = w3.to_checksum_address(data['to'])
    private_key = data['private_key']
    value = w3.to_wei(data['amount'], 'ether')

    tx = {
        'nonce': w3.eth.get_transaction_count(sender),
        'to': receiver,
        'value': value,
        'gas': 21000,
        'gasPrice': w3.to_wei('50', 'gwei')
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()