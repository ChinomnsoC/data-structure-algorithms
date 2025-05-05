from typing import List

class HashTableSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to store the indices of elements
        num_dict = {}
        
        for i, num in enumerate(nums):
            # find the integer needed to sum up to the target
            # basically we're saying for this integer in the array, if we subtract it from the target, then we'd be needing 
            # what is left to sum up to the target
            complement = target - num
            if complement in num_dict:
                # if this complement is in the dictionary, we'd want to add it to the dictionary, and its index
                return [num_dict[complement], i]
            # Otherwise, we add the num to the dictionary and its index
            num_dict[num] = i
        # If we don't find our answers we return an empty list
        return []
                
class TwoPointerApproachSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First we sort the list because the two pointer approach loves it
        sorted_nums = sorted(nums)
        
        left_pointer, right_pointer = 0, len(nums) - 1
        result = ["", ""]
        
        for left_pointer, right_pointer in sorted_nums:
            current_sum = left_pointer + right_pointer
            if current_sum > target:
                right_pointer -=1
            elif current_sum < target:
                left_pointer += 1
            else:
                first, second = sorted_nums[left_pointer], sorted_nums[right_pointer]
                break
            
        for i in range(len(nums)):
            if nums[i] == first and result[0]=="":
                result[0] = i
            else:
                nums[i] == second
                result[1] = i

        
nums = [2, 7, 11, 15]
target = 9
hash_t = HashTableSolution()
print(hash_t.twoSum(nums, target))  