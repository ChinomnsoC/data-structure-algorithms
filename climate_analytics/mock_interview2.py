# **Problem 1:**

# Given a string `s` and an integer `k`, find the length of the longest substring that 
# contains at most `k` distinct characters.

# ```
# Input: s = "eceba", k = 2
# Output: 3  # "ece"

# Input: s = "aa", k = 1
# Output: 2  # "aa"
# ```

# Complexity: O(n) time, O(k) space.
def longest_substring_in_k_distinct(s, k):
    if len(s) < k or not s or not k:
        return 0
    
    char_map = {}
    
    left, right = 0, 0
    
    max_length = 0
    
    for right in range(len(s)):
        char = s[right]
        char_map[char] = char_map.get(char, 0) + 1
        
        
        while len(char_map) > k:
            left_char = s[left]
            char_map[left_char] -= 1
            
            if char_map[left_char] == 0:
                del char_map[left_char]
            
            left += 1
        
        
        max_length = max(max_length, (right - left + 1))
        
    return max_length


print(longest_substring_in_k_distinct(s = "eceba", k = 2))


# **Problem 2:**

# Given an array of integers `nums` and an integer `target`, 
# return the indices of the two numbers that add up to `target`. Assume exactly one solution exists.

# ```
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# ```


def two_sum(nums, target):
    if not nums:
        return []
    
    nums_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in nums_dict:
            return [nums_dict[complement], i]
        
        nums_dict[num] = i
    
    return []


print(two_sum(nums = [3, 2, 4], target = 6))