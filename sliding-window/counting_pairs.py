def count_unique_pairs(nums, k):
    if len(nums) < 2:
        return 0
    left, right = 0, len(nums)-1
    counter = 0
    # arr = [5, 6, 5, 7, 7, 8]
    # target = 13
    
    while left < right:
        sum_of_pairs = nums[left] + nums[right]
        if sum_of_pairs < k:
            left_value = nums[left]
            while left < len(nums) and nums[left] == left_value:
                left += 1
        elif sum_of_pairs > k:
            right_value = nums[right]
            while right >=0 and nums[right] == right_value:
                right -= 1
        else:
            counter += 1
            left_value = nums[left]
            right_value = nums[right]
            while left < len(nums) and nums[left] == left_value:
                left += 1
            while right >=0 and nums[right] == right_value:
                right -= 1
    
    return counter