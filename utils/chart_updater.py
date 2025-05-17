def update_chart(app):
    app.ax.clear()
    app.ax.plot(app.slippage_history[-100:])
    app.ax.set_title("Slippage Over Time")
    app.ax.set_xlabel("Ticks")
    app.ax.set_ylabel("Slippage (%)")
    app.canvas.draw()
