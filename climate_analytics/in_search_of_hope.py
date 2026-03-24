# **In Search of Hope (IDB)**

# Given a 2D matrix and an integer `gas`:
# - `.` = empty land
# - `c` = car (starting position)
# - `o` = oasis (destination)
# - `r` = obstacle (cannot pass)
# - Integer `k` in the matrix = gas station that refuels `k` units

# Traversing one unit consumes 1 gas. You can move up, down, left, right.

# ```
matrix = [
    ['.', '.', '.', 'c', '.'],
    ['.', '.', 'r', 2, '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'o', 'r', '.']
]
gas = 2
# ```

# **Part 1:** Return `True` if car can reach oasis with given gas.
# **Part 2:** There may be a gas station `k` in the matrix — car gains `k` gas units when it passes through. Can car still reach oasis?
# **Part 3:** There are obstacles `r` — car cannot pass through them.
from collections import deque

def in_search_of_hope(matrix, gas):
    # get start location and end location
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "c":
                start_row, start_col = row, col
            if matrix[row][col] == "o":
                end_row, end_col = row, col
    
    # set the remaining gas, queue, and visited
    # remaining_gas = gas
    queue = deque([(start_row, start_col, gas)])
    visited = {}
    
    while queue:
        row, col, remaining_gas = queue.popleft()
        
        if isinstance(matrix[row][col], int):
            remaining_gas += matrix[row][col]
        
        # here we check that we've gotten to the end grid and gas is valid
        if row == end_row and col == end_col:
            return True
        
        # add current row, col to visited
        if (row, col) in visited and visited[(row, col)] >= remaining_gas:
            continue
        
        visited[(row, col)] = remaining_gas
            
        # get the neighbours
        for next_row, next_col in get_4_directions(row, col):
            # validate that it is not out of bound
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or matrix[next_row][next_col] == "r":
                # update to check for obstacle later
                continue
            
            # if the next row, col we're looking at is not in visited, add to visited, and add to queue
            if remaining_gas > 0:
                queue.append((next_row, next_col, remaining_gas - 1))
    
    return False
            
            


def get_4_directions(row, col):
    neighbours = []
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        next_row, next_col = row+dr, col+dc
        neighbours.append((next_row, next_col))
        
    return neighbours
        

print(in_search_of_hope(matrix, gas))
        

