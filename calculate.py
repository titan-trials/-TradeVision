"""calculate.py
Indicator helpers used by the notebook and scripts.

Changes made:
- Case-insensitive column lookup for DataFrame-based indicators (works with Alpaca and yfinance outputs).
- Small RSI safety: avoids noisy divisions and returns a finite series.
"""

def _get_column_case_insensitive(df, name):
    """Return the column from df whose name matches `name` case-insensitively.
    Raises KeyError if not found.
    """
    lower = name.lower()
    for col in df.columns:
        if col.lower() == lower:
            return df[col]
    raise KeyError(f"Column '{name}' not found (case-insensitive search) in DataFrame columns: {list(df.columns)}")


def calculate_sma(prices, window):
    return prices.rolling(window=window).mean()


def calculate_ema(prices, window):
    return prices.ewm(span=window, adjust=False).mean()


def calculate_macd(prices):
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)
    return ema_12 - ema_26


def calculate_rsi(prices, window=14):
    """Calculate RSI using Wilder's smoothing (EMA with adjust=False).

    Returns a pandas Series with the same index as `prices`.
    """
    delta = prices.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    # Use exponential moving average (Wilder's) for smoothing
    avg_gain = gain.ewm(span=window, adjust=False).mean()
    avg_loss = loss.ewm(span=window, adjust=False).mean()

    # Avoid division by zero: when avg_loss == 0 => RSI should be 100 when avg_gain > 0
    rs = avg_gain / avg_loss.replace(0, float('nan'))
    rsi = 100 - (100 / (1 + rs))

    # Where avg_loss == 0 and avg_gain == 0 set RSI to 50 (neutral),
    # where avg_loss == 0 and avg_gain > 0 set RSI to 100
    rsi = rsi.fillna(0)
    mask_gain_zero = (avg_gain == 0) & (avg_loss == 0)
    rsi[mask_gain_zero] = 50.0
    mask_loss_zero_gain_pos = (avg_loss == 0) & (avg_gain > 0)
    rsi[mask_loss_zero_gain_pos] = 100.0

    return rsi


def calculate_dmi(df, period=14):
    """Calculate smoothed +DM and -DM series (Directional Movement) case-insensitively.

    Returns (plus_dm_smoothed, minus_dm_smoothed) as pandas Series with the same index as df.
    The function supports DataFrames with column names like 'high'/'low' or 'High'/'Low'.
    """
    high = _get_column_case_insensitive(df, 'high')
    low = _get_column_case_insensitive(df, 'low')

    up_move = high.diff()
    down_move = low.shift(1) - low

    plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
    minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)

    # Wilder-style smoothing: use alpha = 1/period (equivalent to span ~ period for ewm)
    plus_dm_smoothed = plus_dm.ewm(alpha=1.0 / period, adjust=False).mean()
    minus_dm_smoothed = minus_dm.ewm(alpha=1.0 / period, adjust=False).mean()

    return plus_dm_smoothed, minus_dm_smoothed

