# Conversion Query
# You are given a list of currency conversion rates and a query. 
# Each rate is a triplet [fromCurrency, toCurrency, rate] meaning 1 unit of fromCurrency = rate units of toCurrency.
# Given a query [price, initialCurrency, finalCurrency], return the final converted amount.
rates = [
    ["EUR", "USD", 1.0006],
    ["USD", "JPY", 144.39],
    ["GBP", "USD", 1.1529]
]

# query = [100, "EUR", "JPY"]
# Output: 14441.7... 
# # EUR → USD → JPY
# # 100 * 1.0006 * 144.39
# The conversion path may involve multiple intermediate currencies.

from collections import defaultdict


def conversion_query(rates, query):
    # build adj list
    rates_graph = defaultdict(list)
    
    for source, destination, rate in rates:
        rates_graph[source].append((destination, rate))
    
    visited = set()
    
    if not rates or not query:
        return
    
    amount, start_curr, end_curr = query
    
    if start_curr not in rates_graph:
        return
    
    # write dfs method
    def dfs(current_curr, curr_amount):
        visited.add(current_curr)
        
        if current_curr == end_curr:
            return curr_amount
        
        for neighbour, rate in rates_graph[current_curr]:
            if neighbour not in visited:
                new_amount = curr_amount * rate
                result = dfs(neighbour, new_amount)
                
                if result is not None:
                    return result
        
        return None
    
    return dfs(start_curr, amount)


print(conversion_query(rates, [100, "EUR", "JPY"]))