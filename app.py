from flask import Flask, jsonify
from web3 import Web3
import os

app = Flask(__name__)

# Oneness network configuration
ONENESS_URL = "https://u1ya1ctwrr:6CJgFceo9uCbYNrA8LHUFA1mNI1K-0w1jYDC6XwL8ks@u1rvejyoym-u1ao88tlma-rpc.us1-azure.kaleido.io/"
CHAIN_ID = 989898666
ACCOUNTS = ["4dcc19ef6f937fe9a0f30d2e398d23682fa2696763d6c160d067f93bd6dbbfdf"]

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(ONENESS_URL))

if not web3.isConnected():
    raise Exception("Failed to connect to the Oneness network.")

@app.route('/total_supply', methods=['GET'])
def get_total_supply():
    try:
        # Approximate total supply by fetching the latest block number and multiplying by block reward
        latest_block = web3.eth.block_number
        block_reward = 2  # Example block reward; adjust based on actual network parameters
        total_supply = latest_block * block_reward
        return jsonify({"total_supply": total_supply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/circulating_supply', methods=['GET'])
def get_circulating_supply():
    try:
        # Circulating supply estimation would require tracking burned or locked tokens, which is not straightforward
        # Here, we'll return the same as total supply for simplicity
        latest_block = web3.eth.block_number
        block_reward = 2  # Example block reward; adjust based on actual network parameters
        circulating_supply = latest_block * block_reward
        return jsonify({"circulating_supply": circulating_supply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/price', methods=['GET'])
def get_price():
    return jsonify({
        "error": "Fetching ETH price directly from the blockchain is not supported without an external data source or oracle."
    }), 501

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
