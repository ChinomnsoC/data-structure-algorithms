def tallest_tree_root_variation(forest: dict) -> int:
    if not forest:
        return 0
    
    children = set(forest.keys())
    all_nodes = set(forest.keys()) | set(forest.values())
    
    roots = all_nodes - children
    
    # build the adjacency list
    adj_list = {}
    
    for child, parent in forest.items():
        if parent not in adj_list:
            adj_list[parent] = []
        
        adj_list[parent].append(child)
    
    # write the dfs recursion
    def dfs_height(node, adj_list):
        # check if node in adj_list -- do something
        if node not in adj_list:
            return 1
        # check if child is in adj list
        # can replace with this
        # return 1 + max(dfs_height(child, adj_list) for child in adj_list[node])
        max_height = 0
        for child in adj_list[node]:
            max_height = max(max_height, dfs_height(child, adj_list))
        return 1 + max_height
    
    root_map = {}
    for root in roots:
        height = dfs_height(root, adj_list)
        root_map[root] = height
    
    max_root_height = max(root_map.values())
    
    ties = []
    for root, height in root_map.items():
        if height == max_root_height:
            ties.append(root)
    
    return min(ties)
        
        

    # call dfs on all each root in roots
    # return the min node with max height
 
def tallest_tree_root(forest: dict) -> int:
    if not forest:
        return 0

    # get the childrend and parents ina set
    # build adj list
    # dfs recursion
    # forest is {child: parent}
    children = set(forest.keys())
    all_nodes = set(forest.keys()) | set(forest.values())
    roots = all_nodes - children

    adj_list = {}

    for child, parent in forest.items():
        if parent not in adj_list:
            adj_list[parent] = []
        adj_list[parent].append(child)

    def dfs_height(node, adj_list):
        if node not in adj_list:
            return 1
        return 1 + max(dfs_height(child, adj_list) for child in adj_list[node])

    roots_dictionary = {}
    for root in roots:
        height = dfs_height(root, adj_list)
        roots_dictionary[root] = height

    max_height = max(roots_dictionary.values())

    ties = []
    for root, height in roots_dictionary.items():
        if height == max_height:
            ties.append(root)

    return min(ties)


def do_tests_pass() -> bool:
    assert tallest_tree_root({2: 3, 3: 5, 4: 5, 8: 9}) == 5
    assert tallest_tree_root({1: 2, 3: 4}) == 2  # tie, return smaller
    assert tallest_tree_root({1: 2, 3: 2, 4: 2}) == 2
    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
