# High-Performance-Real-Time-Trade-Cost-Analytics-on-OKX-Spot-Exchange

📈 Overview
This project is a real-time trading cost analytics simulator built for the OKX Spot market. It connects to OKX’s WebSocket L2 orderbook feed and dynamically estimates:

Slippage (via regression modeling)

Fees (rule-based on tier)

Market Impact (using Almgren-Chriss model)

Net Cost

Maker/Taker Probability (via logistic regression)

Internal Latency (processing latency per tick)

The system features a user-friendly GUI for configuring trade parameters and viewing computed outputs live.

🧠 Features
✅ Input Parameters (Left Panel)
Exchange: OKX (hardcoded)

Asset Pair: Select from available spot pairs (e.g., BTC-USDT)

Order Type: Market (default)

Quantity: Input (e.g., 100 USD equivalent)

Volatility: Fetched from market data

Fee Tier: Based on OKX documentation

📤 Output Parameters (Right Panel)
Estimated Slippage: Based on linear/quantile regression

Expected Fees: Tiered fee structure

Market Impact: Almgren-Chriss model

Net Cost: Aggregated cost (Slippage + Fee + Impact)

Maker/Taker Proportion: Predicted using logistic regression

Latency: Processing time per L2 update

🧩 Technologies Used
Component	Technology
Language	Python 3.10+
WebSocket	websockets, asyncio
UI	tkinter
Modeling	scikit-learn, numpy, pandas
Plotting (if used)	matplotlib or plotly
Logging	logging
Performance	time, asyncio
