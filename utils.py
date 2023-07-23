import talib 


class indicators:

    def __init__(self,data):
        self.data = data 

    def calculate_moving_average(self, data, window):
        return talib.SMA(data, window)

# Function to calculate relative strength index (RSI)
    def calculate_rsi(self, data, window):
        return talib.RSI(data, window)
    

