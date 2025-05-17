import asyncio
import json
import time
import websockets
from models.estimators import (
    estimate_slippage_val, fees_amount, market_impact,
    predict_maker_taker_proportion
)
from utils.chart_updater import update_chart

async def websocket_handler(app):
    URL = "wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP"
    async with websockets.connect(URL) as ws:
        while True:
            start_time = time.time()
            msg = await ws.recv()
            end_time = (time.time() - start_time) * 1000

            data = json.loads(msg)
            Biding_price = data['bids']
            Asking_price = data['asks']
            app.orderbook_data = (Biding_price, Asking_price)

            order_size = app.amount.get()
            slippage_value = estimate_slippage_val(order_size, Asking_price)
            brokrage_fees = fees_amount(order_size, app.fee_rate)
            impact = market_impact(order_size, app.volatility)
            Total_net_cost = slippage_value + brokrage_fees + impact
            proportion = predict_maker_taker_proportion([slippage_value, brokrage_fees, impact])

            app.slippage_val.set(f"{slippage_value:.4f}")
            app.brokrage_val.set(f"{brokrage_fees:.4f}")
            app.impact_val.set(f"{impact:.4f}")
            app.netcost_val.set(f"{Total_net_cost:.4f}")
            app.proportion_val.set(f"{proportion:.4f}")
            app.latency_val.set(f"{end_time:.2f} ms")

            app.slippage_history.append(slippage_value)
            update_chart(app)

def start_websocket(app):
    asyncio.new_event_loop().run_until_complete(websocket_handler(app))
