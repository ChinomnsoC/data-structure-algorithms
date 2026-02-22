from typing import List


def optimal_path(grid: List[List[int]]) -> int:
    """
    Find the maximum number of rocks that can be collected
    traveling from bottom-left (So_Cal) to top-right (New_York).
    Can only move north (up) or east (right).

    Args:
        grid: 2D list where grid[row][col] represents rocks at that position
              Bottom-left is start (So_Cal), top-right is end (New_York)

    Returns:
        Maximum rocks that can be collected
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    print(rows, cols)
    
    # [[0, 0, 0, 0, 5], 
    #  [0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0]]
    

    
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    print(dp)
    
    end_row = 0
    end_col = cols-1
    # dp_end= grid[0][cols-1]
    
    dp[end_row][end_col] = grid[end_row][end_col]

    # TODO: Implement the optimal path algorithm
    
    for j in range(cols-2, -1, -1):
        dp[0][j] = grid[0][j] + dp[0][j+1]
        
    for i in range(1, rows):
        for j in range(cols-1, -1, -1):
            if i == end_row and j == end_col:
                dp[i][j] = grid[i][j]
                continue
            print(f"i= {i}, j= {j}")
            move_north = dp[i-1][j] if i > 0 else 0
            print(move_north)
            move_east = dp[i][j+1] if j < cols - 1 else 0
            
            dp[i][j] = grid[i][j] + max(move_north, move_east)
            print(dp[i][j])
            
    print(dp)
    print(dp[rows-1][0])
    return dp[rows-1][0]

def do_tests_pass() -> bool:
    """Test cases for the rock collector problem"""

    # Test case from the problem description
    grid1 = [
        [0, 0, 0, 0, 5],  # New York (top row)
        [0, 1, 1, 1, 0],  # Middle row
        [2, 0, 0, 0, 0],  # So_Cal (bottom row)
    ]
    # Expected path: 2 -> 0 -> 1 -> 1 -> 1 -> 0 -> 5 = 10
    
    grid2 = [
        [0, 1, 8, 0, 5],
    ]
    
    grid3 = [
        [1, 0, 1, 4, 5],  # New York (top row)
        [0, 1, 0, 1, 0],  # Middle row
        [2, 8, 4, 0, 0],  # So_Cal (bottom row)
    ]
    
    return optimal_path(grid1) == 10 and optimal_path(grid2) == 14 and optimal_path(grid3) == 24


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
