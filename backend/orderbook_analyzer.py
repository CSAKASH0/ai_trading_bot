import requests

def get_orderbook_metrics(symbol):
    url = f"https://api.backpack.exchange/api/v1/orderbook/{symbol}"
    resp = requests.get(url).json()

    bids = resp.get('bids', [])
    asks = resp.get('asks', [])

    volume = sum([float(b[1]) for b in bids]) + sum([float(a[1]) for a in asks])
    bid_density = len(bids)
    ask_density = len(asks)
    depth = abs(float(bids[0][0]) - float(asks[0][0])) if bids and asks else 0

    return {
        "volume": volume,
        "bid_density": bid_density,
        "ask_density": ask_density,
        "depth": depth
    }