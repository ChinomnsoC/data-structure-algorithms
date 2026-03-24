# <!-- **Aggregate Trades — Union Find**

# Given a list of trades and a list of symbol equivalences, aggregate total trade values for each unique company.


trades = [
    ("TSLA US Equity", 500), 
    ("TSLA US Equity", 600), 
    ("VOD LN Equity", 1000), 
    ("TSLA UW Equity", 250)
]
equivalences = [
    ("TSLA US Equity", "TSLA UB Equity"), 
    ("TSLA UB Equity", "TSLA UW Equity"), 
    ("VOD LN Equity", "VOD IN Equity")
]
# Output: [("TSLA US Equity", 1350), ("VOD LN Equity", 1000)]

# Symbols linked directly or indirectly belong to the same company. -->

def aggregate_trades(trades, equivalences):
    parent = {}
    totals = {}
    
    def find(trade_x):
        if parent[trade_x] != trade_x:
            parent[trade_x] = find(parent[trade_x])
        
        return parent[trade_x]
    
    def union(trade_x, trade_y):
        root_x = find(trade_x)
        root_y = find(trade_y)
        
        if root_x != root_y:
            parent[root_x] = root_y
    
    # 1. Initialise every symbol as its own parent
    # (from both trades and equivalences)
    
    for pair in equivalences:
        trade_x, trade_y = pair
        parent[trade_x] = trade_x
        parent[trade_y] = trade_y
    
    for trade in trades:
        symbol, price = trade
        parent[symbol] = symbol
    
    # 2. Union all equivalent symbols
    for pair in equivalences:
        trade_x, trade_y = pair
        union(trade_x, trade_y)
    
    
    # 3. For each trade, find its root and add to totals
    
    for trade in trades:
        symbol, price = trade
        root = find(symbol)
        totals[root] = totals.get(root, 0) + price
    
    # 4. Return aggregated totals
    
    return list(totals.items())

print(aggregate_trades(trades, equivalences))