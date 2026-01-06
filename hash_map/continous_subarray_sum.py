def check_subarray_sum(nums, k):
        
    remainder_map = {}
    remainder_map[0] = -1
    running_sum = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        key = running_sum % k
        if key not in remainder_map:
            remainder_map[key] = i
            print("key and value", key, i)
        else:
            value = remainder_map[key]
            print("key and value", value, key)
            length_of_sub_array = abs(value - i)
            # print("length_of_sub_array", length_of_sub_array)
            if length_of_sub_array >= 2:
                print("value and i", value, i)
                print(f"sub array: [{nums[value+1]}, {nums[i]}]")
                return True
    # Return this placeholder return statement with your code
    return False
