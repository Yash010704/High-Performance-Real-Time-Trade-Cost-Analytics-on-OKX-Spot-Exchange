import tkinter as tk
from tkinter import ttk
import threading
from gui.components import setup_inputs, setup_outputs, setup_chart
from services.websocket_handler import start_websocket

class TradingSimulatorApp:
    def __init__(self, node):
        self.root = node
        self.root.title("OKX Trade Simulator")

        self.input_frame = ttk.LabelFrame(node, text="Input Parameters")
        self.output_frame = ttk.LabelFrame(node, text="Output Values")
        self.chart_frame = ttk.LabelFrame(node, text="Slippage Chart")

        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        self.output_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')
        self.chart_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        setup_inputs(self)
        setup_outputs(self)
        setup_chart(self)

        self.orderbook_data = None
        self.volatility = 0.02
        self.fee_rate = 0.001
        self.latency_val.set("Waiting for data...")
        self.slippage_history = []

        threading.Thread(target=lambda: start_websocket(self), daemon=True).start()
