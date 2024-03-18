from statistics import median
from typing import List

class Solution:
    # O((m+n)log(m+n)) time complexity
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list =sorted(nums1 + nums2)
        new_list_length = len(new_list)
        print(new_list_length)
        
        
        if new_list_length % 2 == 0:
            midi1 = new_list[new_list_length//2]
            midi2 = new_list[new_list_length//2 - 1]
            median_number = (midi1 + midi2)/2
            print(f"Midi1: {midi1}")
            print(f"Midi2: {midi2}")
        else:
            median_number = new_list[new_list_length//2]
            print(f"Odd number length: {median_number}")
        return median_number
        
        
            


nums1 = [1, 2, 3, 4, 5, 6] 
nums2 = [7, 8, 9] 
median_sorted = Solution()
print(median_sorted.findMedianSortedArrays(nums1, nums2))