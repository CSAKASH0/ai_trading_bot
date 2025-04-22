from flask import Flask, request, jsonify
from trading_bot import generate_signal
from image_trend_detector import analyze_uploaded_chart
from orderbook_analyzer import get_orderbook_metrics
from wallet_manager import get_balance, send_transaction
from trade_logger import log_trade
from db.init_db import init_trade_db, init_wallet_db

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    address = request.json["address"]
    return jsonify({"status": "connected", "wallet": address})

@app.route("/api/balance/<wallet>")
def balance(wallet):
    return jsonify({"balance": get_balance(wallet)})

@app.route("/api/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    tx_hash = send_transaction(data)
    return jsonify({"tx_hash": tx_hash})

@app.route("/api/trend", methods=["POST"])
def trend():
    file = request.files['file']
    result = analyze_uploaded_chart(file)
    return jsonify(result)

@app.route("/api/signal", methods=["POST"])
def signal():
    data = request.json
    result = generate_signal(data['symbol'])
    return jsonify(result)

@app.route("/api/orderbook", methods=["GET"])
def orderbook():
    symbol = request.args.get('symbol')
    result = get_orderbook_metrics(symbol)
    return jsonify(result)

if __name__ == "__main__":
    init_trade_db()
    init_wallet_db()
    app.run(debug=True)