from typing import List, Tuple
from collections import deque


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
        return []

    def is_valid_position(self, row: int, col: int, grid: List[List[int]]) -> bool:
        """Check if position is within bounds and not blocked."""
        # TODO: Implement bounds checking
        return True

    def calculate_walking_distance(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> int:
        """Calculate Manhattan distance between two points."""
        # TODO: Implement distance calculation
        return 0


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
