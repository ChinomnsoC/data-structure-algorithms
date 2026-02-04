# Multi-Currency Hotel Payment Optimization
# Scenario: You're building Booking.com's payment processing system. A customer wants to book a hotel, but the optimal payment route isn't always direct due to varying conversion fees and currency availability.
# Problem: Given currency conversion rates with fees, find the cheapest way to pay for a hotel booking.
# Input:

# currencies: List of available currencies ["USD", "EUR", "GBP", "JPY"]
# conversions: List of [from_currency, to_currency, exchange_rate, fee_percentage]
# customer_currency: Currency customer has
# hotel_currency: Currency hotel accepts
# amount: Amount to pay in hotel currency
# max_conversions: Maximum conversion steps allowed (to avoid complex chains)

# Output: Minimum total cost in customer's currency, or -1 if impossible
# Example:
# currencies = ["USD", "EUR", "GBP", "JPY"]
# conversions = [
#     ["USD", "EUR", 0.85, 2.0],    # 1 USD → 0.85 EUR, 2% fee
#     ["EUR", "USD", 1.18, 1.5],   # 1 EUR → 1.18 USD, 1.5% fee  
#     ["USD", "GBP", 0.75, 3.0],   # 1 USD → 0.75 GBP, 3% fee
#     ["GBP", "EUR", 1.12, 1.0],   # 1 GBP → 1.12 EUR, 1% fee
#     ["USD", "JPY", 110, 0.5]     # 1 USD → 110 JPY, 0.5% fee
# ]
# customer_currency = "USD"
# hotel_currency = "EUR"  
# amount = 1000  # Need 1000 EUR
# max_conversions = 2

# Expected: Should find cheapest path USD→EUR vs USD→GBP→EUR
# Your task: Implement findCheapestConversion(currencies, conversions, customer_currency, hotel_currency, amount, max_conversions)

def reverse_conversion(from_curr, to_curr, rate, fee):
    effective_rate = rate * (1 - fee/100)
    return [to_curr, from_curr, 1/effective_rate, fee]

# setup for bellman ford
def findCheapestConversion(currencies, conversions, customer_currency, hotel_currency, amount, max_conversions):
    
    reversed_conversions = []
    
    for conv in conversions:
        reversed_conversions.append(reverse_conversion(conv[0], conv[1], conv[2], conv[3]))
    
    cost = {curr: float("inf") for curr in currencies}
    cost[hotel_currency] = amount
    
    for i in range(max_conversions + 1):
        temp_cost = cost.copy()
        
        for from_curr, to_curr, rate, fee in reversed_conversions:
            if cost[from_curr] == float("inf"):
                continue
            
            converted_amount = cost[from_curr] * rate
            if converted_amount < temp_cost[to_curr]:
                temp_cost[to_curr] = converted_amount
            
        cost = temp_cost
        
    
    return - 1 if cost[customer_currency] == float('inf') else cost[customer_currency]
    