def circular_array_loop(nums):  
    false_sample_list = [2,1,-1,-2]
    true_sample_list = [3,3,1,-1,2]
    n = len(nums)
    
    fast_pointer, slow_pointer = 0, 0
    
    while fast_pointer < n and fast_pointer + 1 < n:
        slow_pointer = slow_pointer + 1
        fast_pointer = fast_pointer + 2
        # count slow_pointer by the value of nums[slow_pointer], then when we get to the new position, repeat.
        # if we're able to repeat the top again and again until we get to the initial value of nums[slow_pointer], return true
        # let circular_array_loop return true
        # 
        

    return False