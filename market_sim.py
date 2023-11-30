import random
import matplotlib.pyplot as plt

class Trader:
    def __init__(self, strategy):
        self.strategy = strategy
        self.stocks = 0
        self.cash = 10000  # Initial cash

    def make_decision(self, price):
        if self.strategy == "buy_low_sell_high":
            if price < 100:  # Buy condition
                self.stocks += int(self.cash / price)
                self.cash -= self.stocks * price
            elif price > 150 and self.stocks > 0:  # Sell condition
                self.cash += self.stocks * price
                self.stocks = 0
        # More strategies can be added here

# Market simulation
def market_simulation(num_traders, num_days):
    traders = [Trader("buy_low_sell_high") for _ in range(num_traders)]
    price = 100  # Initial stock price
    price_history = []

    for _ in range(num_days):
        for trader in traders:
            trader.make_decision(price)
        
        # Update price based on supply and demand
        demand = sum(trader.stocks for trader in traders)
        supply = num_traders * 1000 - demand
        price += (demand - supply) / 10000
        price_history.append(price)

    return price_history

# Simulate the market
num_traders = 100
num_days = 200
price_history = market_simulation(num_traders, num_days)

# Plotting
plt.plot(price_history)
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Financial Market Simulation')
plt.show()
