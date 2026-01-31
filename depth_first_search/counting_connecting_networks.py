# You have a graph of n nodes.
# You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.
from typing import List


class Solution:

    def count_connected_networks(self, n: int, edges: List):
        """
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        Output: 1
        """
        # adj_list
        # dfs
        adj_list = [[] for _ in range(n)]

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()
        connected_network_count = 0

        def dfs(node):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                connected_network_count += 1

        return connected_network_count


counting = Solution()
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(counting.count_connected_networks(n, edges))
