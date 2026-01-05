def min_subarray_len(nums, s):
    
    running_sum = 0
    left, right = 0, 0
    best_answer = float('inf')
    
    for right in range(len(nums)):
        running_sum += nums[right]
        while running_sum >= s:
            window= right - left + 1
            best_answer = min(window, best_answer)
            running_sum -= nums[left]
            left += 1
    if best_answer == float('inf'):
        return 0
    else:
        return best_answer