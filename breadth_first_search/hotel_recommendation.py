from typing import List, Tuple
from collections import deque


# Questions
# expecting only positive integers in the rating and walking distance? can they be null?
# What exactly should we return?
# If I've understood correctly, we want to rank the hotels first by distance to user's location, then by star rating
# then by row cordinate, then by column cordinate?
# Is it possible for any of the arguements to be missing?
# What happens if we don't find hotel(s) that fit at all or if the user wants 3 but there are only 2?
class HotelRecommendationSystem:
    """
    Booking.com Hotel Search System

    You're building a feature that helps users find hotels within walking distance
    of tourist attractions. Given a city grid where:
    - 0 = blocked area (water, construction, etc.)
    - 1 = walkable area
    - 2+ = hotel with that star rating (2=2-star, 3=3-star, etc.)

    Find hotels within walking distance that match user preferences.
    """

    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    def find_nearby_hotels(
        self,
        city_grid: List[List[int]],
        user_location: List[int],
        max_walking_distance: int,
        min_star_rating: int,
        max_results: int,
    ) -> List[List[int]]:
        """
        Find hotels within walking distance that meet criteria.

        Args:
            city_grid: 2D grid representing the city
            user_location: [row, col] where user is located
            max_walking_distance: maximum blocks user will walk
            min_star_rating: minimum hotel star rating required
            max_results: maximum number of hotels to return

        Returns:
            List of hotel locations [[row, col], ...] ranked by:
            1. Distance (closer first)
            2. Star rating (higher rating first for ties)
            3. Row coordinate (smaller first)
            4. Column coordinate (smaller first)
        """
        # TODO: Implement this method
        start_row, start_col = user_location[0], user_location[1]
        depth = 0

        queue = [(start_row, start_col, depth)]
        visited_location = set()
        valid_hotel = []  # depth, rating, row_cord, col_cord

        while queue:
            row, col, depth = queue.pop(0)

            # traversal check
            if (
                (row, col) in visited_location
                or self.is_out_of_bounds(row, col, city_grid)
                or depth > max_walking_distance
                or city_grid[row][col] == 0
            ):
                print("is out of bounds or too much depth or blocked area")
                continue

            visited_location.add((row, col))
            # valid position check

            cell_value = city_grid[row][col]
            if cell_value >= min_star_rating:
                print(
                    f"Found valid item at ({row},{col}) with value {cell_value} at distance {depth}"
                )
                hotel_rating = city_grid[row][col]
                valid_hotel.append((depth, hotel_rating, row, col))

            for next_row, next_col in self.get_next_neighbors(row, col):
                print("adding to queue", next_row, next_col)
                queue.append((next_row, next_col, depth + 1))

            # navigate to the next position in the grid
            # need to implement a method that helps me get the next neighbour if we are still at depth < max walking distance

        valid_hotel.sort(key=lambda x: (x[0], -x[1], x[2], x[3]))
        results = []
        for depth, hotel_rating, row, col in valid_hotel:
            if len(valid_hotel) >= max_results:
                results = [
                    [row, col]
                    for depth, hotel_rating, row, col in valid_hotel[:max_results]
                ]    
            elif len(valid_hotel) > 0:
                results.append([row, col])
                
        return results

    def is_out_of_bounds(self, row, col, grid):
        row_length = len(grid)
        col_length = len(grid[0])

        return row < 0 or row >= row_length or col < 0 or col >= col_length

    def get_next_neighbors(self, row, col):
        neighbor = []

        for dr, dc in self.directions:
            new_row, new_col = row + dr, col + dc
            neighbor.append((new_row, new_col))

        return neighbor


# Test cases - DO NOT MODIFY
def test_hotel_system():
    system = HotelRecommendationSystem()

    # Test case 1: Basic hotel search
    city1 = [[1, 2, 1, 4], [1, 0, 1, 1], [3, 1, 1, 5], [1, 1, 0, 1]]
    result1 = system.find_nearby_hotels(city1, [0, 0], 3, 2, 3)
    expected1 = [[0, 1], [2, 0], [0, 3]]
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Expected: {expected1}, Got: {result1}")

    # Test case 2: Distance limit
    result2 = system.find_nearby_hotels(city1, [0, 0], 2, 2, 5)
    expected2 = [[0, 1], [2, 0]]
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Expected: {expected2}, Got: {result2}")


if __name__ == "__main__":
    test_hotel_system()
