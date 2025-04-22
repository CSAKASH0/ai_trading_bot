import ccxt
import pandas as pd
import ta

def generate_signal(symbol):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1h', limit=100)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['ema_short'] = ta.trend.EMAIndicator(df['close'], window=9).ema_indicator()
    df['ema_long'] = ta.trend.EMAIndicator(df['close'], window=21).ema_indicator()

    if df['rsi'].iloc[-1] < 30 and df['ema_short'].iloc[-1] > df['ema_long'].iloc[-1]:
        return {"signal": "buy"}
    elif df['rsi'].iloc[-1] > 70 and df['ema_short'].iloc[-1] < df['ema_long'].iloc[-1]:
        return {"signal": "sell"}
    else:
        return {"signal": "hold"}