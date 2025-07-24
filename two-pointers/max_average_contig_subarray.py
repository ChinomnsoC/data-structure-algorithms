import statistics
 # if length of nums <= k, find mean of nums and return float answer
        # initialise left at 0 and right at k-1
        # calculate the average of all the numbers from left to right.
        # convert to int, compare max with max_avg
        # update max_avg with the max
        # [1,0,1,4,2,5,6]
        # then move left one step forward, and right too

def findMaxAverage(nums, k):
    if len(nums) <= k:
        return sum(nums)/k
    
    left, right = 0, k - 1
    current_sum = sum(nums[left:right + 1])
    curr_avg = current_sum/k
    
    max_avg = curr_avg
    
    while right < len(nums) - 1:
        left += 1
        right += 1
        
        current_sum = current_sum - nums[left - 1] + nums[right]
        curr_avg = current_sum/k
        print(curr_avg, "curr_avg", max_avg)
        
        print("curr_avg vs max_avg", curr_avg, max_avg)
        max_avg = max(max_avg, curr_avg)
        
    
    return max_avg


our_list = [4433,-7832,-5068,4009,2830,6544,-6119,-7126,-780,-4254,-8249,-9168,9492,402,5789,6808,8953,5810,-7353,7933,4766,5182,-3230,-1989,5786,6922,-4646,4415,-9906,807,-6373,3370,2604,8751,-9173,-2668,-6876,9500,3465,-1900,4134,-1758,-1453,-5201,-9825,4469,-1999,-1108,1836,3923,6796,-5252,9863,-5997,-3251,9596,-3404,-540,2826,-1737,3341,-3623,-9885,2603,-5782,8174,2710,6504,-4128]

# Final output
print("\nMax:")
print(findMaxAverage(our_list, 59))