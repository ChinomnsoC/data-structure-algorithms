import time
from collections import deque

transactions = []


def call_three_times():
    now = time.time()
    
    transactions.append(now)
    
    if len(transactions) == 3:
        earliest = transactions.pop(0)
        return now - earliest < 3
    
    return False


queue = deque()

def more_than_three():
    time_now = time.time()
    three_seconds_ago = time_now - 3
    
    queue.append(time_now)
    while queue and queue[0] < three_seconds_ago:
        queue.popleft()
    
    return len(queue) > 3