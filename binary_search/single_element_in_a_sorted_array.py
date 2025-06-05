from collections import Counter

# Just playing here :)
# def single_non_duplicate(nums):
#     answer = Counter(nums)
#     last_single = [key for key, val in answer.items() if val == 1][-1]
#     print(answer)
#     return last_single

def single_non_duplicate(nums):
    n = len(nums)
    left, right = 0, n-1
   
    while left != right:
        mid_index = left + (right - left) // 2
        if mid_index % 2 == 1:
            print("odd")
            mid_index -= 1
        # If nums[mid] and nums[mid + 1] are not the same integers, move the right pointer towards left.
        if nums[mid_index] != nums[mid_index + 1]:
            right = mid_index
            print(nums[mid_index], nums[mid_index + 1])
            print("right, mid_index", right, mid_index)
        # Otherwise, if nums[mid] and nums[mid + 1] are the same, move left towards right.
        else:
            print(nums[mid_index], nums[mid_index + 1])
            left = mid_index + 2
            print("left, mid_index", left, mid_index)
        
    return nums[left]
number = [0,0,1,1,2,2,4,8,8,16,16,32,32]
print(single_non_duplicate(number))