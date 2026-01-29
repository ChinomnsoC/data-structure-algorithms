from typing import List


class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        low_price_band, high_price_band = pricing[0], pricing[1]
        start_row, start_col = start[0], start[1]
        depth = 0

        queue = [(start_row, start_col, 0)]
        visited = set()
        valid_items = []

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
                valid_items.append((depth, cell_value, row, col))

            for next_row, next_col in self.get_next_neighbour(row, col):
                queue.append((next_row, next_col, depth + 1))

        valid_items.sort()

        return [[row, col] for depth, price, row, col in valid_items[:k]]

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
