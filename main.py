import tkinter as tk
from gui.app import TradingSimulatorApp

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("900x600")
    app = TradingSimulatorApp(root)
    root.mainloop()
