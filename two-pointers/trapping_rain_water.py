from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        height_length = len(height)

        for i in range(height_length):
            max_height_left = 0

            for left_location in range(i):
                max_height_left = max(height[left_location], max_height_left)

            max_height_right = 0
            for right_location in range(i + 1, height_length):
                max_height_right = max(height_length[right_location], max_height_right)

            shorter_wall = min(max_height_left, max_height_right)
            if height[i] < shorter_wall:
                water_trapped = shorter_wall - height[i]
                result += water_trapped

        return result

    def trap_precompute_method(self, height: List[int]) -> int:
        total_trapped = 0
        height_length = len(height)

        if height_length <= 2:
            return 0

        left_max = [0] * height_length
        left_max[0] = height[0]
        for i in range(1, height_length):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max = [0] * height_length
        right_max[height_length - 1] = height[height_length - 1]
        for i in range(height_length - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(height_length):
            shorter_wall = min(left_max[i], right_max[i])
            if height[i] < shorter_wall:
                total_trapped += shorter_wall - height[i]

        return total_trapped
