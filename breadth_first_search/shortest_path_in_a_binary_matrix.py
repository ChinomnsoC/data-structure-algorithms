from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited_cell_count = 1

        visited = set()
        start_row, start_col = 0, 0
        rows = len(grid)
        cols = len(grid[0])
        end_row, end_col = rows - 1, cols - 1

        if grid[start_row][start_col] == 1 or grid[end_row][end_col] == 1:
            return -1

        queue = [(start_row, start_col, visited_cell_count)]

        while queue:
            row, col, visited_cell_count = queue.pop(0)

            # if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 1:
            #     continue
            if row == end_row and col == end_col:
                return visited_cell_count

            if (row, col) not in visited:
                visited.add((row, col))

            for next_row, next_col in self.get_8_direction_neighbours(row, col):
                if (
                    next_row < 0
                    or next_row >= rows
                    or next_col < 0
                    or next_col >= cols
                    or grid[next_row][next_col] == 1
                ):
                    # out of bounds or invalid
                    continue
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, visited_cell_count + 1))

        return -1

    def get_8_direction_neighbours(self, row, col):
        neighbours = []

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (1, -1),
            (-1, 1),
            (1, 1),
        ]

        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            neighbours.append((next_row, next_col))

        return neighbours

