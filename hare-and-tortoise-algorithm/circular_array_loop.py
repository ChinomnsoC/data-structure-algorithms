# def circular_array_loop(nums):  

#     n = len(nums)
    
#     # fast_pointer, slow_pointer = 0, 0
    
#     # while fast_pointer < n and fast_pointer + 1 < n:
#     #     # slow_pointer = slow_pointer + 1
#     #     # fast_pointer = fast_pointer + 2
        
#     #     move_direction = nums[slow_pointer] > 0
#     #     # count slow_pointer by the value of nums[slow_pointer], then when we get to the new position, repeat.
#     #     # if we're able to repeat the above again and again until we get to the initial value of nums[slow_pointer], return true
#     #     # let circular_array_loop return true
#     #     # 
    
#     for i in range(n):
#         direction = nums[i] >= 0
#         fast_pointer, slow_pointer = i, i
        
#         while True:
#             move_direction = nums[i] > 0
#             if direction != move_direction:
#                 return -1
            
#             next_index = (i + nums[i]) % n
#             slow_pointer = 
        

#     return False

# false_sample_list = [2,1,-1,-2]
# true_sample_list = [3,3,1,-1,2]
# output = circular_array_loop(true_sample_list)


def count_length_of_cycle(arr, start_index):
    
    slow, fast = start_index, start_index
    
    for _ in range(len(arr)):
        slow = arr[slow]
        fast = arr[arr[fast]]
        
        if slow == fast:
            # we've found a cycle
            break
    else:
        return -1
        # starting from current position of slow, increment slow until we get back to current slow position.
        # count the increment.
        # return the number.
    meeting_point = slow
    slow = arr[slow]
    counter = 1
    
    while slow != meeting_point:
        slow = arr[slow]
        counter += 1

    return counter


def do_tests_pass():
    return (
        count_length_of_cycle([1, 0], 1) == 2 and
        count_length_of_cycle([1, 2, 0], 0) == 3
    )

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")