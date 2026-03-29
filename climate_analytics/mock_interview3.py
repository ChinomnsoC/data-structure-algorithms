# **Problem 1:**

# Given a list of trades and their stock symbols, and a list of symbol equivalences, aggregate the total trade value for each unique company.

# ```python
trades = [
    ("TSLA US Equity", 500),
    ("TSLA UW Equity", 250),
    ("VOD LN Equity", 1000),
]

equivalences = [
    ("TSLA US Equity", "TSLA UB Equity"),
    ("TSLA UB Equity", "TSLA UW Equity"),
]

# Output: [("TSLA US Equity", 750), ("VOD LN Equity", 1000)]
# ```

class AggregateTrades:
    def __init__(self, trades, equivalences):
        self.trades = trades
        self.equivalences = equivalences
        self.parent = {}
        self.totals = {}
    
    def find(self, tradeX):
        if self.parent[tradeX] != tradeX:
            self.parent[tradeX] = self.find(self.parent[tradeX])
            
        return self.parent[tradeX]
    
    def union(self, tradeX, tradeY):
        root_x = self.find(tradeX)
        root_y = self.find(tradeY)
        
        if root_x != root_y:
            self.parent[root_x] = root_y
        
    def aggregate_trades(self):
        
        for pair in self.equivalences:
            tradeX, tradeY = pair
            self.parent[tradeX] = tradeX
            self.parent[tradeY] = tradeY
        
        for trade in self.trades:
            symbol, price = trade
            self.parent[symbol] = symbol
            
        
        for pair in self.equivalences:
            tradeX, tradeY = pair
            self.union(tradeX, tradeY)
            
        for trade in self.trades:
            symbol, price = trade
            
            root = self.find(symbol)
            self.totals[root] = self.totals.get(root, 0) + price
        
        return list(self.totals.items())
    

aggregates = AggregateTrades(trades=trades, equivalences=equivalences)

print(aggregates.aggregate_trades())



# **Problem 2:**

# Given an array of integers, return the length of the longest consecutive sequence.

# ```
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4  # [1, 2, 3, 4]

# Input: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9  # [0,1,2,3,4,5,6,7,8]
# ```

# Must run in O(n) time. You're on.

def longest_consecutive_sequence(input):
    if not input:
        return 0
    input_set = set(input)

    max_sequence_length = 0
    for num in input_set:
        if num - 1 not in input_set:
            sequence_length = 1
            while num + sequence_length in input_set:
                sequence_length += 1
            max_sequence_length = max(max_sequence_length, sequence_length)
    return max_sequence_length

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))