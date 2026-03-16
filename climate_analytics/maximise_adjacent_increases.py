# Maximise Adjacent Increases
# You are given an array of integers ratings representing the scores of different entities. You can rearrange these ratings in any order you choose.
# Your goal is to find the maximum possible number of indices i (where 1≤i<n) such that ratings[i] > ratings[i-1].
# Example:
# Input: ratings = [2, 1, 3, 3, 2, 1]
# Output: 4
# Explanation: One optimal rearrangement is [1, 2, 3, 1, 2, 3].
# 2>1 (Yes)
# 3>2 (Yes)
# 1>3 (No)
# 2>1 (Yes)
# 3>2 (Yes)
# Total count: 4.

# This is just maths. When you have an array, get the freq of each value.
# the best possible answer is N - 1
# the worst possible answer is 0
# in between there can be duplicates. with each duplicate we lose the possibility of reaching n -1  by 1 point.
# more accurately, the unique value with the most duplicates is what determines how many 1 points we;d be removing from our
# best possible solution


def maximise_adj_increases(arr):
    if not arr:
        return 0
    array_map = {}
    n = len(arr)
    
    
    for val in arr:
        array_map[val] = array_map.get(val, 0) + 1
        
    # distinct_val_in_arr = len(array_map)
    
    max_freq = max(array_map.values())
    
    return n - max_freq
    
print(maximise_adj_increases([-1])) # == 0
print(maximise_adj_increases([1, -9, 3, 5, 3])) # -9, 1, 3, 5, 3 == 3
print(maximise_adj_increases([-3, -4, -4, -8])) # -8, -4, -3, -4 == 2
print(maximise_adj_increases([2, 2, 2, 2, 2, 2])) # == 0 (no increase)
print(maximise_adj_increases([2, 1, 3, 3, 2, 1])) # 1, 2, 3, 1, 2, 3 == 4
print(maximise_adj_increases([]))

