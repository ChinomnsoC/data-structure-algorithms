# **Word Search (LC 79)**

# ```python
board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

# word = "ABCCED"  # → True
# word = "SEE"     # → True  
# word = "ABCB"    # → False
# ```

def word_search(board, word):
    
    visited = set()
    rows = len(board)
    cols = len(board[0])
    
    
    def dfs(row, col, word_index, visited):
        if word_index == len(word):
            return True
        
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        
        if (row, col) in visited:
            return False
        
        if board[row][col] != word[word_index]:
            return False
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        visited.add((row, col))
        
        for dr, dc in directions:
            next_row, next_col = dr + row, dc + col
            if dfs(next_row, next_col, word_index + 1, visited):
                return True   
            
        visited.remove((row, col))
        return False     
    
    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0, set()):
                return True
    
    return False



print(word_search(board, "ABCCED"))

# Time complexity — more precise: O(m × n × 4^L) where L is the length of the word. 
# At each cell you can branch 4 directions, up to L levels deep.
# Space: O(L) for the recursion stack and visited set, where L is word length.