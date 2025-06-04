def find_closest_elements(nums, k, target):
    n = len(nums)
    if n == k:
        return nums
    #  If the target is smaller than the smallest 
    #  element or larger than the largest, return either the first or last k elements.
    if target < nums[0]:
        return nums[:k]
    elif target > nums[n-1]:
        return nums[k-1:]


number = [1,2,3,4,5]
print(find_closest_elements(number, 3, -1))