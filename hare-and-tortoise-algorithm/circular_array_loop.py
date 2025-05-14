def circular_array_loop(nums):  

    n = len(nums)
    
    # fast_pointer, slow_pointer = 0, 0
    
    # while fast_pointer < n and fast_pointer + 1 < n:
    #     # slow_pointer = slow_pointer + 1
    #     # fast_pointer = fast_pointer + 2
        
    #     move_direction = nums[slow_pointer] > 0
    #     # count slow_pointer by the value of nums[slow_pointer], then when we get to the new position, repeat.
    #     # if we're able to repeat the above again and again until we get to the initial value of nums[slow_pointer], return true
    #     # let circular_array_loop return true
    #     # 
    
    for i in range(n):
        direction = nums[i] >= 0
        fast_pointer, slow_pointer = i, i
        
        while True:
            move_direction = nums[i] > 0
            if direction != move_direction:
                return -1
            
            next_index = (i + nums[i]) % n
            slow_pointer = 
        

    return False

false_sample_list = [2,1,-1,-2]
true_sample_list = [3,3,1,-1,2]
output = circular_array_loop(true_sample_list)