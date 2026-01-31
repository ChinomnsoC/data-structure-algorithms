
def count_connected_components(n, edges):
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
    # updated adj list [[1], [0, 2], [1, 3], []]

    for node in range(n):
        if node not in visited_node:
            queue.append(node)
            # queue = [0]
            while queue:
                current_node = queue.pop(0)
                # node = 1
                if current_node not in visited_node:
                    visited_node.add(current_node)

                    for neighbor in adj_list[current_node]:
                        if neighbor not in visited_node:
                            queue.append(neighbor)
                            visited_node.add(neighbor)
            connected_component_count += 1


def display_adj_list(adj_list):

    for i in range(len(adj_list)):
        print(f"{i}: ", end="")
        for j in adj_list[i]:
            print(f"{j} ", end="")
        print()


# Test cases
def test():
    # Test 1: Basic case
    result1 = count_connected_components(6, [[5, 1], [4, 3]])
    print(f"Test 1: Expected 4, Got {result1}")

    # Test 2: All connected
    result2 = count_connected_components(4, [[0, 1], [1, 2], [2, 3]])
    print(f"Test 2: Expected 1, Got {result2}")

    # Test 3: All isolated
    result3 = count_connected_components(3, [])
    print(f"Test 3: Expected 3, Got {result3}")


if __name__ == "__main__":
    test()