# 📊 SMC Trading Bot (GBPJPY – 15 Minute Timeframe)

## 📌 Project Overview

This project implements a **rule-based Smart Money Concepts (SMC) trading bot** using Python.  
It analyzes **GBP/JPY forex price data** on a **15-minute timeframe** to generate trading signals based on market structure and institutional trading concepts.

The system performs a **basic backtest**, logs trading signals to CSV files, and calculates simplified profit and performance metrics.

> ⚠️ **Disclaimer**  
> This project is for **educational purposes only** and does not constitute financial advice.

---

## 🧠 Concepts Implemented

- Smart Money Concepts (SMC)
- Swing High & Swing Low Detection
- Break of Structure (BOS)
- Fair Value Gaps (FVG)
- Liquidity Zones
- Order Blocks (OB)
- Risk Management & Position Sizing
- Backtesting with CSV logging

---

## 🗂 Project Structure




---

## 📥 Input Data

- **Instrument:** GBP/JPY
- **Timeframe:** 15 Minutes
- **Format:** CSV

Expected CSV format (no header):

| Column | Description |
|------|------------|
| pair | Currency pair |
| timestamp | Date & time |
| open | Open price |
| close | Close price |

Since only `open` and `close` are available, **high and low values are approximated**:

- `high = max(open, close)`
- `low = min(open, close)`

---

## ⚙️ Core Components

### 1️⃣ Data Loading & Preprocessing
- Loads raw CSV data
- Converts timestamps
- Approximates missing OHLC values
- Resamples data to 15-minute candles

---

### 2️⃣ Signal Data Model

```python
@dataclass
class Signal:
    side: str
    entry: float
    stop: float
    take_profit: float
    reason: str

# Performance metrics
signals_log.csv
signals_with_profit.csv

#HOW TO RUN
1.install all dependencies
pip install numpy pandas
2.update CSV path
df = pd.read_csv('/path/to/GBPJPY_15m.csv', header=None)
3.Run the script
python smc_bot.py


⚠️ Limitations
Approximated high/low prices
No spread, slippage, or commissions
Simplified profit calculations
Not suitable for live trading


🚀 Future Improvements
Use real OHLC data
Add session filters (London / New York)
Improve risk modeling
Integrate with live trading APIs
Enhance backtesting realism

🎓 Educational Use
This project demonstrates:
Algorithmic trading logic
Financial data analysis
Risk-based decision making
Python programming for Digital Business & FinTech


📜 License
This project is provided for educational use only.
