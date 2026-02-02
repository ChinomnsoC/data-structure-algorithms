# The problem: Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.
# Example:
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1


def numIslands(grid):
    if not grid:
        return 0

    island_count = 0

    rows, cols = len(grid), len(grid[0])
    #   0 1 2 (x)
    # 0
    # 1.  X(x=1, y=1)
    # 2
    # (y)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row, col):
        # base case for marking out of bound

        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1":
            return
        
        grid[row][col] = "0"
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            dfs(next_row, next_col)
        

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                island_count += 1
                dfs(row, col)
                
    return island_count
