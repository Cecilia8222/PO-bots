import numpy as np
import pandas as pd

class CandlestickPatterns:
    def __init__(self, data):
        self.data = data

    def engulfing_pattern(self):
        # Identify Bullish and Bearish Engulfing Patterns
        engulfing = []
        for i in range(1, len(self.data)):
            if (self.data['Close'][i] > self.data['Open'][i] and 
                self.data['Close'][i-1] < self.data['Open'][i-1] and 
                self.data['Close'][i] > self.data['Open'][i-1] and 
                self.data['Open'][i] < self.data['Close'][i-1]):
                engulfing.append((i, 'Bullish'))
            elif (self.data['Close'][i] < self.data['Open'][i] and 
                  self.data['Close'][i-1] > self.data['Open'][i-1] and 
                  self.data['Close'][i] < self.data['Open'][i-1] and 
                  self.data['Open'][i] > self.data['Close'][i-1]):
                engulfing.append((i, 'Bearish'))
        return engulfing

    def zigzag_pattern(self, deviation=5):
        # Simple zigzag pattern detection
        zigzag = []
        high = self.data['High'][0]
        low = self.data['Low'][0]
        direction = None

        for i in range(1, len(self.data)):
            if self.data['High'][i] > high:
                high = self.data['High'][i]
                if direction == 'down':
                    zigzag.append((i-1, 'Peak'))
                    direction = 'up'
            elif self.data['Low'][i] < low:
                low = self.data['Low'][i]
                if direction == 'up':
                    zigzag.append((i-1, 'Trough'))
                    direction = 'down'
        return zigzag

    def candle_color_analysis(self):
        # Analyze candle colors for bullish or bearish trends
        colors = []
        for i in range(len(self.data)):
            if self.data['Close'][i] > self.data['Open'][i]:
                colors.append('Bullish')
            else:
                colors.append('Bearish')
        return colors

# Example usage:
# df = pd.read_csv('your_data.csv') # Load your data here
# patterns = CandlestickPatterns(df)
# print(patterns.engulfing_pattern())  
# print(patterns.zigzag_pattern())    
# print(patterns.candle_color_analysis())