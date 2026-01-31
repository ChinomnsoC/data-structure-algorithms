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