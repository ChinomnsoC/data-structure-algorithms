def is_valid_tree(n, edges):
    if len(edges) != n-1:
        return False
    
    adj_list = [[] for _ in range(n)]
    
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    print(adj_list)
    visited = set()
    
    def dfs(node, parent):
        print("something")
        visited.add(node)
        
        for neighbour in adj_list[node]:
            
            # if not visited
            if neighbour not in visited:
                if not dfs(neighbour, node):
                    return False
            
            # if visited
            elif neighbour != parent:
                # neighbour not a parent but it is visited already
                return False
                
        return True
        
    for node in range(n):
        if node not in visited:
            if not dfs(node, -1):
                return False
            
    print(adj_list)
        
    if len(visited) != n:
        return False
    return True

n = 4
edges = [[0,1],[2,3]]

print(is_valid_tree(n, edges))

# Cycle detection in an undirected graph
# Question 1

# You are given an undirected graph represented as an adjacency list. Each node is labeled with a unique integer from 0 to n-1. Write a function that determines whether the graph is a valid tree.

# A valid tree is a connected graph with no cycles.

# Input:

# n (int): The number of nodes in the graph.
# edges (List[List[int]]): The list of undirected edges, where each edge is represented as a pair [u, v].
# Output:

# Return True if the graph is a valid tree, otherwise return False.
# Constraints:

# 1 <= n <= 10^4
# 0 <= edges.length <= 10^4
# 0 <= u, v < n
# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: True
# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: False