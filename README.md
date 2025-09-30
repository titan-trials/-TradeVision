# -Quantara
simulator for financial markets. Integrated multiple technical indicator  with risk management features to evaluate trading strategies. Designed to track performance metrics such as ROI, drawdown, and Sharpe ratio. Long-term goal: extend the system into a machine learning driven model that autonomously generates buy/sell decisions.

## THIS IS A PLACE TO TRACK MY PROGRESS AS I WORK THROUGH MAKING THIS AND EVENTUALLY FINISHING IT.
## I KNOW NOTHING ABOUT CODING AND I AM LEARNING AS I GO :)


To do (In order of what needs to be done): 
    1. Add More Indicators:
        RSI (Relative Strength Index): Identifies overbought/oversold conditions (Best for trading ranges in of trend market)
            https://www.investopedia.com/terms/r/rsi.asp
                Divergences
                Adjusting to trends
                Posiitve-Negative Reversals
                RSI Swings

        MACD (Moving Average Convergence Divergence): Detects trend shifts (Lagging Indicator)
            https://www.investopedia.com/terms/m/macd.asp#toc-what-is-macd
            
            [best used with daily data](https://www.investopedia.com/ask/answers/122414/how-reliable-using-moving-average-convergence-divergence-macd-create-or-follow-trading-strategies.asp)
            
                Note: MACD is best used with daily periods, where the traditional settings of 26/12/9 days is the default.
                MACD = 12-Period EMA - 26-Period EMA
                When 12 == 26 (at two points) base line created
                **KEY NOTE BELOW**
                    Both measure the momentum of an instrument, but they measure different factors. The two can sometimes give contradictory results. The RSI may show a reading above 70 (overbought) for a sustained period, indicating an instrument is overextended to the buy side. In contrast, the MACD may indicate that the instrument’s buy-side momentum is still growing. Either indicator may signal an upcoming trend change by showing divergence from price (price continues higher while the indicator turns lower, or vice versa).
                    Confirmation should be sought by trend-following indicators, such as the Directional Movement Index (DMI) system and its key component, the Average Directional Index (ADX).

        Bollinger Bands: Measures volatility; great for mean reversion                  
        ADX (Average Directional Index): Measures trend strength

    2. Enhance Trade Logic based on 1 and 2
        i.e.
        if short > long: buy
        Try:
        if (short > long) and (RSI < 70) and (MACD > 0): buy
        Reason: Multiple confirmations reduce false signals

    3.Add Risk Management
        Add a stop-loss (e.g., -5%) and take-profit (e.g., +10%) mechanism
        Allow position sizing based on capital or risk per trade
        Track drawdown and risk metrics

    4. Add Backtest Visualization
        Add arrows to plot buy/sell signals
        Drawdown chart, equity curve

    5. Add Strategy Evaluation Metrics
        After each simulation:
            Profit/Loss
            Win Rate
            Sharpe Ratio
            Max Drawdown
            CAGR

    6. Portfolio Level Backtest
        Allocate capital to multiple tickers
        Track total capital over time
        Rebalancing logic

    7. Strategy Customization:
        Allow users to select which indicators and rules to use via input

    8. Parameter Optimization
        Use Grid Search to optimize:
            Short/Long EMA windows
            RSI thresholds
            Stop loss/take profit values
    
    9. Data Enhancements:
        Use higher frequency data (intraday) or alternative data sources

    10. Machine Learning:
        Use ML models to predict price direction or classify signals
    
