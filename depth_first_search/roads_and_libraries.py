# The algorithm:

# Find all connected components and their sizes
# For each component, calculate the cheaper strategy
# Sum all component costs
# Compare total with "library everywhere" cost
# Return minimum

def roadsAndLibraries(n, c_lib, c_road, cities):
    if n == 1:
        return c_lib
    
    if c_lib <= c_road:
        return n * c_lib
    
    library_everywhere_cost = n * c_lib
    
    adj_list = [[] for _ in range(n)]
    
    for city in cities:
        node1, node2 = city[0] - 1, city[1] - 1 # for 0 based indexing used in hackerrank
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    connected_component_count = 0
    visited = set()
    
    # get the size of a connected network
    # get the total of connected networks
    
    
    def dfs(node):
        visited.add(node)
        k = 1 # size of each connected network
        
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                k += dfs(neighbour)
        
        return k

    total_optimal_cost = 0
    for node in range(n):
        if node not in visited:
            k = dfs(node)
            connected_component_count += 1
            cost_of_library_in_every_city_in_this_network = calc_library_in_every_city_in_this_network(k, c_lib)
            cost_of_one_library_in_this_network = calc_one_library_per_network(c_lib, c_road, k)
        
            total_optimal_cost += min(cost_of_library_in_every_city_in_this_network, cost_of_one_library_in_this_network)
            
    
    return min(total_optimal_cost, library_everywhere_cost)

#  For each connected component of size k:

# Option A: k * c_lib (library in every city of this component)
# Option B: c_lib + (k-1) * c_road (1 library + roads to connect all cities)
# Choose min(Option A, Option B) for each component

def calc_library_in_every_city_in_this_network(k, c_lib):
    return k * c_lib

def calc_one_library_per_network(c_lib, c_road, k):
    return c_lib + (k-1) * c_road