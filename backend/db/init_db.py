import sqlite3

def init_trade_db():
    conn = sqlite3.connect("db/trade_history.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            action TEXT,
            price REAL,
            volume REAL,
            timestamp TEXT
        );
    """)
    conn.commit()
    conn.close()

def init_wallet_db():
    conn = sqlite3.connect("db/wallet_txns.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS txns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet TEXT,
            tx_hash TEXT,
            action TEXT,
            value REAL,
            token TEXT,
            timestamp TEXT
        );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_trade_db()
    init_wallet_db()