# **Trading Symbols Set (IDB)** = Insert Delete GetRandom O(1) (LC 380)

# Design a data structure for a trading platform to manage a dynamic set of stock symbols. 
# Support all operations in **average O(1)** time:

# - `add(symbol)` — add symbol to the set
# - `remove(symbol)` — remove symbol from the set  
# - `getRandom()` — return a uniformly random symbol from the current set

# ```
# add("AAPL")
# add("TSLA")
# add("GOOG")
# remove("TSLA")
# getRandom() → "AAPL" or "GOOG" with equal probability
# ```
import random

class TradingSymbols:
    def __init__(self):
        self.symbol_dictionary = {}
        self.list_of_symbols = []
        
    def add(self, symbol):
        
        if not symbol or symbol in self.symbol_dictionary:
            return
        
        self.list_of_symbols.append(symbol)
        self.symbol_dictionary[symbol] = len(self.list_of_symbols) - 1
    
    def remove(self, symbol):
        if not symbol or symbol not in self.symbol_dictionary:
            return
        
        # get current position of symbol
        position = self.symbol_dictionary.pop(symbol)
        
        # if position is not the last item in list
        if position != len(self.list_of_symbols) - 1:
            # pop the last item in the list
            last_symbol_in_list = self.list_of_symbols.pop()
            # set the last item in the lsit to be the positio iof the sysmbol we want to remove
            self.symbol_dictionary[last_symbol_in_list] = position
            # set the position in the list to be the former last symbol
            self.list_of_symbols[position] = last_symbol_in_list
        else:
            self.list_of_symbols.pop()
    
    def getRandom(self):
        return random.choice(self.list_of_symbols)


trading_symbols = TradingSymbols()

trading_symbols.add("AAPL")
trading_symbols.add("TSLA")
trading_symbols.add("GOOG")
trading_symbols.add("VUAG")
trading_symbols.remove("TSLA")
print(trading_symbols.getRandom()) # → "AAPL" or "GOOG" with equal probability