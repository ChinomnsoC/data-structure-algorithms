# **Flag Transactions (IDB)** = Invalid Transactions (LC 1169)

# Given a list of transactions in the format `{name, time, amount, city}`, return all invalid transactions.

# A transaction is invalid if:
# - `amount > 1000`, OR
# - The same name has another transaction in a **different city** within **±60 minutes**

# O(n²) worst case for the comparison loop. O(n) space.

# ```python
transactions = [
    {"name": "alice", "time": 20, "amount": 800, "city": "london"},
    {"name": "alice", "time": 50, "amount": 100, "city": "paris"},
    {"name": "bob",   "time": 10, "amount": 1200, "city": "london"},
    {"name": "mannua",   "time": 10, "amount": 100, "city": "london"},
]

# Output: [
#     {"name": "alice", "time": 20, ...},  # same name, different city within 60 mins
#     {"name": "alice", "time": 50, ...},  # same name, different city within 60 mins
#     {"name": "bob",   "time": 10, ...},  # amount > 1000
# ]
# ```


class FlagTransactions:
    def __init__(self, transactions):
        self.transactions = transactions
        self.transaction_map = {}
        self.invalid_indices = set()

        for i, transaction in enumerate(self.transactions):
            if transaction["name"] not in self.transaction_map:
                self.transaction_map[transaction["name"]] = []

            self.transaction_map[transaction["name"]].append(
                (transaction["time"], transaction["city"], i)
            )
            if transaction["amount"] > 1000:
                self.invalid_indices.add(i)

        # "alice": [(20, "london", 0), (50, "paris", 1)],

        for _, list_of_transactions in self.transaction_map.items():
            if len(list_of_transactions) > 1:
                for i in range(len(list_of_transactions)):
                    time_1, city_1, index_1 = list_of_transactions[i]
                    for j in range(len(list_of_transactions)):
                        time_2, city_2, index_2 = list_of_transactions[j]

                        if abs(time_1 - time_2) <= 60 and city_1 != city_2:
                            self.invalid_indices.add(index_1)
                            self.invalid_indices.add(index_2)  

    def flag_transactions(self):
        return [self.transactions[i] for i in self.invalid_indices]


ft = FlagTransactions(transactions)

print(ft.flag_transactions())