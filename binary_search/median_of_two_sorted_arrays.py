def median_of_two_sorted_arrays(sorted_a, sorted_b):
    if not sorted_a and not sorted_b:
        return 0
    
    # this way, sorted_a is always the shorter list
    if len(sorted_a) > len(sorted_b):
        sorted_a, sorted_b = sorted_b, sorted_a
    
    m = len(sorted_a)
    n = len(sorted_b)
    
    left, right = 0, m
    
    while left <= right:
        partition_in_a = (left + right) // 2
        partition_in_b = (m + n + 1) // 2 - partition_in_a
        
        # [1, 3, 5, 6, 9, 10]
        
        a_left_max = sorted_a[partition_in_a-1] if partition_in_a > 0 else float('-inf')
        a_right_min = sorted_a[partition_in_a] if partition_in_a < m else float('inf')
        b_left_max = sorted_b[partition_in_b - 1] if partition_in_b > 0 else float('-inf')
        b_right_min = sorted_b[partition_in_b] if partition_in_b < n else float('inf')
        
        
        if a_left_max <= b_right_min and b_left_max <= a_right_min:
            if (m + n) % 2 == 1:
                return max(a_left_max, b_left_max)
            
            else:
                return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2
        elif a_left_max > b_right_min:
            right = partition_in_a - 1
        
        else:
            left = partition_in_a + 1
def do_test_pass():

    
    result1 = median_of_two_sorted_arrays([1,3], [2,4])
    result2 = median_of_two_sorted_arrays([1,3,5], [2,4])
    result3 = median_of_two_sorted_arrays([-5,-3,7], [-2,4,6])
    result4 = median_of_two_sorted_arrays([], [1,2,3])
    result5 = median_of_two_sorted_arrays([], [])
    return result1 == 2.5 and result2 == 3 and result3 == 1.0 and result4 == 2 and result5 == 0


    
if __name__ == "__main__":
    if do_test_pass():
        print("All tests pass")
    else:
        print("Test failed")