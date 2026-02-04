# 1. Initialize costs: cost[src] = 0, all others = infinity
#    cost[0] = 0, cost[1] = infinity, cost[2] = infinity

# 2. For stops in range(k + 1):  # k=0, so range(1) = [0]
#    3. For each flight [from_city, to_city, price] in flights:
#       4. If cost[from_city] + price < cost[to_city]:
#          5. cost[to_city] = cost[from_city] + price

# 6. Return cost[dst] if cost[dst] != infinity else -1

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")] * n
        cost[src] = 0
        
        
        for i in range(k+1):
            
            temp_cost = cost.copy()
            for start_city, stop_city, price in flights:
                if cost[start_city] == float("inf"):
                    continue
                if cost[start_city] + price < temp_cost[stop_city]:
                    temp_cost[stop_city] = cost[start_city] + price
            
            cost = temp_cost
        
        return cost[dst] if cost[dst] != float("inf") else -1
    