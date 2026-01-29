from typing import List
from heapq import heappush, heapreplace

# there's a serious bug in this code

class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        low_price_band, high_price_band = pricing[0], pricing[1]
        start_row, start_col = start[0], start[1]
        depth = 0

        queue = [(start_row, start_col, 0)]
        visited = set()
        valid_items_min_heap = []

        while queue:
            row, col, depth = queue.pop(0)

            if (
                (row, col) in visited
                or self.out_of_bounds(row, col, grid)
                or grid[row][col] == 0
            ):
                continue

            visited.add((row, col))

            cell_value = grid[row][col]

            if cell_value >= low_price_band and cell_value <= high_price_band:
                # we have a valid item!
                # valid_items_min_heap.append((depth, cell_value, row, col))
                print(f"Found valid item at ({row},{col}) with value {cell_value} at distance {depth}")
                
                item = (depth, cell_value, row, col)
                
                if len(valid_items_min_heap) < k:
                    heappush(valid_items_min_heap, item)
                elif item < valid_items_min_heap[0]:
                    heapreplace(valid_items_min_heap, item)

            for next_row, next_col in self.get_next_neighbour(row, col):
                queue.append((next_row, next_col, depth + 1))

        valid_items_min_heap.sort()

        return [[row, col] for depth, price, row, col in valid_items_min_heap]

    def out_of_bounds(self, row, col, grid):
        row_length = len(grid)
        col_length = len(grid[0])

        return row < 0 or row >= row_length or col < 0 or col >= col_length

    def get_next_neighbour(self, row, col):

        # up = (-1, 0)
        # down = (1, 0)
        # left = (0, -1)
        # right = (0, 1)

        neighbour = []

        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + d_row, col + d_col

            neighbour.append((new_row, new_col))

        return neighbour
