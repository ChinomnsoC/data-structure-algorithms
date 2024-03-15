
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Here we set the left and right pointers for the Binary search which is
        # the best solution for this. This is just to find the extreme left and right positions
        left_pointer, right_pointer = 0, len(nums)-1


        while left_pointer <= right_pointer:
            # Here we find the mid point of the list, using floor division, returns the middle position
            mid_point = (left_pointer + right_pointer) // 2 
            print(f"mid_point:{mid_point}")
            
            # If the mid point of the list is the target, we return the mid point
            if mid_point == target:
                return mid_point
            #  if the element of the sorted array nums located at the index mid_point is less than the target,
            #  it means the target should be located to the right of mid_point, so we update left to mid + 1 to search in the right half of the array.
            elif nums[mid_point] < target:
                print(f"nums mid_point:{nums[mid_point]}")
                print(f"mid_point again:{mid_point}")
                left_pointer = mid_point + 1
                print(f"left_pointer:{left_pointer}")
            else:
                right_pointer = mid_point - 1
                print(f"right_pointer:{right_pointer}")
            print("first iteration")
        
        return left_pointer
    
    
this_list = [6, 7, 8, 9, 10, 11, 12]
target = 10
binary_search = Solution()
print(binary_search.searchInsert(this_list, target))