import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def setup_inputs(app):
    ttk.Label(app.input_frame, text="Exchange").grid(row=0, column=0, sticky='w')
    app.exchange = ttk.Combobox(app.input_frame, values=["OKX"])
    app.exchange.set("OKX")
    app.exchange.grid(row=0, column=1)

    ttk.Label(app.input_frame, text="Asset").grid(row=1, column=0, sticky='w')
    app.asset = ttk.Combobox(app.input_frame, values=["BTC-USDT-SWAP"])
    app.asset.set("BTC-USDT-SWAP")
    app.asset.grid(row=1, column=1)

    ttk.Label(app.input_frame, text="Order Type").grid(row=2, column=0, sticky='w')
    app.order_type = ttk.Combobox(app.input_frame, values=["market"])
    app.order_type.set("market")
    app.order_type.grid(row=2, column=1)

    ttk.Label(app.input_frame, text="Amount (USD)").grid(row=3, column=0, sticky='w')
    app.amount = tk.DoubleVar(value=100)
    ttk.Entry(app.input_frame, textvariable=app.amount).grid(row=3, column=1)

def setup_outputs(app):
    app.slippage_val = tk.StringVar()
    app.brokrage_val = tk.StringVar()
    app.impact_val = tk.StringVar()
    app.netcost_val = tk.StringVar()
    app.proportion_val = tk.StringVar()
    app.latency_val = tk.StringVar()

    labels = [
        (" Slippage  Value (%)", app.slippage_val),
        ("Brokrage Fees (USD)", app.brokrage_val),
        ("Expected Market Impact", app.impact_val),
        ("Total Net Cost", app.netcost_val),
        ("Maker/Taker Proportion", app.proportion_val),
        ("Internal Latency (ms)", app.latency_val),
    ]

    for i, (text, var) in enumerate(labels):
        ttk.Label(app.output_frame, text=text).grid(row=i, column=0, sticky='w')
        ttk.Label(app.output_frame, textvariable=var).grid(row=i, column=1, sticky='e')

def setup_chart(app):
    app.fig, app.ax = plt.subplots(figsize=(6, 2.5))
    app.ax.set_title("Slippage Over Time")
    app.ax.set_xlabel("Ticks")
    app.ax.set_ylabel("Slippage (%)")
    app.canvas = FigureCanvasTkAgg(app.fig, master=app.chart_frame)
    app.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
