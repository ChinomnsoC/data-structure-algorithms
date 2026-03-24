# **Number of Provinces (LC 547)**

# There are `n` cities. Some are connected directly. A **province** is a group of directly or indirectly connected cities.

# Given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` means city `i` and city `j` are directly connected, 
# return the number of provinces.

# ```
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# ```

# What's your approach?

def number_of_provinces(isConnected):
    
    province_count = 0
    
    n = len(isConnected)
    
    visited = set()
    
    
    
    def dfs(city):
        
        visited.add(city)
        
        for neighbour in range(n):
            if isConnected[city][neighbour] == 1 and neighbour not in visited:
                dfs(neighbour)

    
    for i in range(n):
        if i not in visited:
            province_count += 1
            dfs(i)

    return province_count

print(number_of_provinces([[1,1,0],[1,1,0],[0,0,1]]))
print(number_of_provinces([[1,0,0],[0,1,0],[0,0,1]]))