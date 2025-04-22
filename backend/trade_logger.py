import sqlite3

def log_trade(symbol, action, price, volume):
    conn = sqlite3.connect("db/trade_history.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO trades (symbol, action, price, volume, timestamp)
        VALUES (?, ?, ?, ?, datetime('now'))
    """, (symbol, action, price, volume))
    conn.commit()
    conn.close()


def log_wallet_tx(wallet, tx_hash, action, value, token='ETH'):
    conn = sqlite3.connect("db/wallet_txns.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO txns (wallet, tx_hash, action, value, token, timestamp)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (wallet, tx_hash, action, value, token))
    conn.commit()
    conn.close()