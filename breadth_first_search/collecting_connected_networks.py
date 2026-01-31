def collect_connected_components(n, edges):
    """
    Count the number of connected components in an undirected graph.

    Args:
        n: number of nodes (0 to n-1)
        edges: list of edges [[node1, node2], ...]

    Returns:
        int: number of connected components
    """
    # TODO: implement
    adj_list = [[] for _ in range(n)]

    for edge in edges:
        node1, node2 = edge[0], edge[1]

        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    print("updated adj list", adj_list)
    display_adj_list(adj_list)
    i = 0

    queue = []
    visited_node = set()
    connected_component_count = 0
    all_components = []
    # updated adj list [[1], [0, 2], [1, 3], []]

    for node in range(n):
        if node not in visited_node:
            queue.append(node)
            # queue = [0]
            print("first queue", queue)
            while queue:
                current_component = []
                current_node = queue.pop(0)
                print("current node", current_node)
                # node = 0
                if current_node not in visited_node:
                    visited_node.add(current_node)
                    print("visited_node", visited_node)
                    current_component.append(current_node)
                    print(current_component)
                    # vn = [0]

                    for neighbor in adj_list[current_node]:
                        # n = 1
                        print("neighbor", neighbor)
                        if neighbor not in visited_node:
                            queue.append(neighbor)
                            print("last queue", queue)
                            visited_node.add(neighbor)
                            current_component.append(neighbor)
    
                    all_components.append(current_component)
            connected_component_count += 1
            print("current_component", current_component)
            
    print("all_components", all_components)
    return all_components


def display_adj_list(adj_list):

    for i in range(len(adj_list)):
        print(f"{i}: ", end="")
        for j in adj_list[i]:
            print(f"{j} ", end="")
        print()


# Test cases
def test():
    # Test 1: Basic case
    result1 = collect_connected_components(6, [[5, 1], [4, 3]])
    print(f"Test 1: Expected 4, Got {result1}")

    # Test 2: All connected
    result2 = collect_connected_components(4, [[0, 1], [1, 2], [2, 3]])
    print(f"Test 2: Expected 1, Got {result2}")

    # Test 3: All isolated
    result3 = collect_connected_components(3, [])
    print(f"Test 3: Expected 3, Got {result3}")


if __name__ == "__main__":
    test()
