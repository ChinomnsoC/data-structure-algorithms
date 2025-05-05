from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use two pointers that you update based on the height that is the minimum. 
        # What you want is to maximize the height, so we move in the direction of the height. 
        # - Loop over all numbers, take height to be min between left element and right element
        # - take width to be right - left
        # - if width * height > area→ update area
        # - If value at left pointer is less than value at right pointer → increase left pointer by 1
        # - else reduce right pointer by 1
        # return area
        left, right = 0, len(height)-1
        max_area = 0

        while left < right:
            min_height = min(height[left],height[right])
            width = right - left
            output = min_height * width

            if output > max_area:
                max_area = output
            if height[left] < height[right]:
                left += 1
            else:
                right-= 1