# **Stock Trading (IDB)**

# Given an array of integers where the i-th integer represents the stock price on day i, 
# return the largest possible profit from one transaction (buy one share, sell one share).

# ```
# prices = [1, 2, 3, 4, 5]
# Output: 4  # buy day 1, sell day 5

# 1
# 10

# prices = [4, 5, 2, 1, 6, 10, 4, 9, 11]
# Output: 10  # buy day 4, sell day 9

# prices = [33, 18, 8, 2]
# Output: 0  # no profitable transaction
# ```

# **Follow-up:** What if you can do multiple transactions?

# What's your approach?


def stock_trading(prices):
    min_price = float('inf')
    min_position = -1
    biggest_profit = -1
    max_position = -1
    best_buy = -1
    
    for i, price in enumerate(prices):
        # if curr price is > min price, calculate profit_if_sold_today, 
        # if profit_if_sold_today > biggest_profit, update biggest_profit, i
        print(price, min_price)
        if price < min_price:
            min_price = price
            print("min_price", min_price)
            min_position = i
        
        profit_if_sold_today = price - min_price
        print(profit_if_sold_today)
        
        if profit_if_sold_today > biggest_profit:
            biggest_profit = profit_if_sold_today
            best_buy = min_position
            max_position = i
            print(max_position)

    return [best_buy + 1, max_position + 1] if min_position != float('inf') and max_position != float('inf') and min_position < max_position else 0

# print(stock_trading([4, 5, 2, 1, 6, 10, 4, 9, 11]))
# print(stock_trading([33, 18, 8, 2]))


def stock_trading_multiple_buys(prices):
    running_sum = 0
    i = 0
    
    while i < len(prices) - 1:
        if prices[i] < prices[i+1]:
            running_sum += prices[i+1] - prices[i]
        
        i += 1
        
    return running_sum

print(stock_trading_multiple_buys([4, 5, 2, 1, 6, 10, 4, 9, 11]))