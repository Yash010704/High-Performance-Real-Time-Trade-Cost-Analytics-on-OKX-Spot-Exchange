import numpy as np

def estimate_slippage_val(order_size_usd, orderbook):
    prices, sizes = zip(*[(float(p), float(s)) for p, s in orderbook])
    total = 0
    qty = 0
    for price, size in zip(prices, sizes):
        cost = price * size
        if total + cost >= order_size_usd:
            qty += (order_size_usd - total) / price
            total = order_size_usd
            break
        qty += size
        total += cost
    avg_price = total / qty if qty > 0 else 0
    best_price = prices[0]
    return abs(avg_price - best_price) / best_price * 100

def fees_amount(order_size_usd, fee_rate):
    return order_size_usd * fee_rate

def market_impact(order_size_usd, volatility):
    k = 0.01
    return k * volatility * np.sqrt(order_size_usd)

def predict_maker_taker_proportion(features):
    x = np.array(features)
    return 1 / (1 + np.exp(-np.sum(x)))
