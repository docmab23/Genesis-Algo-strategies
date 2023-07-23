import pandas as pd
import numpy as np
import talib

target_allocation = {
    "SPY" : 0.20,
    "QQQ" : 0.20,
    "PSQ" : 0.20,
    "QLD" : 0.20,
    "SHY" : 0.20
}

current_allocation = {
    "SPY" : 0.25,
    "QQQ" : 0.15,
    "PSQ" : 0.20,
    "QLD" : 0.20,
    "SHY" : 0.20

}


# Function to calculate moving average
def calculate_moving_average(data, window):
    return talib.SMA(data, window)

# Function to calculate relative strength index (RSI)
def calculate_rsi(data, window):
    return talib.RSI(data, window)

# Function to determine target allocations
def determine_target_allocations(data):
    target_allocations = {}  # Dictionary to store target allocations
    # Calculate target allocations based on some logic
    # ...
    return target_allocations

# Function to check if holding differs by 12%+ from its target
def check_holding_difference(current_allocation , target_allocation):
    for i, allocs in enumerate(current_allocation.keys()):
        if abs(current_allocation[allocs] -  target_allocation[allocs]) >= 0.12 * target_allocation[allocs]:
            return True 
        return False 
        
def actual_trade(spy_prices , qqq_prices):
    trade = check_holding_difference(current_allocation, target_allocation)
    if trade: 
     spy_ma_200 = calculate_moving_average(spy_prices, 200)
     qqq_ma_20 = calculate_moving_average(qqq_prices, 20)
     
     if spy_prices[-1] > spy_ma_200[-1]:
        selected_asset = 'QQQ'
     else:
    # Check if QQQ price is below 20-day moving average
       if qqq_prices[-1] < qqq_ma_20[-1]:
        # Calculate relative strength index (RSI) for assets
        psq_rsi = calculate_rsi(psq_prices, 10)  # Replace with actual PSQ prices
        shy_rsi = calculate_rsi(shy_prices, 10)  # Replace with actual SHY prices
        # Determine asset with the highest RSI
        if psq_rsi[-1] > shy_rsi[-1]:
            selected_asset = 'PSQ'
        else:
            selected_asset = 'SHY'
    else:
        selected_asset = 'QQQ'




# Example data for demonstration
spy_prices = [100, 110, 120, 130, 140]  # Replace with actual SPY prices
qqq_prices = [200, 190, 180, 170, 160]  # Replace with actual QQQ prices

# Calculate moving averages

# Determine target allocations


# Check if SPY price is above 200-day moving average

# Perform trades to match target allocations if holding differs by 12%+
for asset, target_allocation in target_allocations.items():
    current_price = get_current_price(asset)  # Replace with function to get current price of asset
    if check_holding_difference(current_price, target_allocation):
        # Perform trade to match target allocation
        # ...

# Print selected asset
  print("Selected Asset:", selected_asset)
