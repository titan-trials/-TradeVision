#Calculations.py
#All indicators & moving average functions

def calculate_sma(prices, window):
    return prices.rolling(window=window).mean()

def calculate_ema(prices, window):
    return prices.ewm(span=window, adjust=False).mean()

def calculate_macd(prices):
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)
    return ema_12 - ema_26

def calculate_rsi(prices, window=14):
    delta = prices.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(span=window, adjust=False).mean()
    avg_loss = loss.ewm(span=window, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calculate_dmi(df, period=14):
    up_move = df['High'].diff()
    down_move = df['Low'].shift(1) - df['Low']
    plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0)
    minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0)
    plus_dm_smoothed = plus_dm.ewm(alpha=1/period, adjust=False).mean()
    minus_dm_smoothed = minus_dm.ewm(alpha=1/period, adjust=False).mean()
    return plus_dm_smoothed, minus_dm_smoothed

