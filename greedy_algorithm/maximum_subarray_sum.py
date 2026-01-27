from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    i, running_total, best_seen_total = 0, 0, float('-inf')
    # [5, 10, 15, 20, 25]

    if n == 1:
        return nums[0]

    
    while i < n:
        start_afresh_total = nums[i]
        print("start_afresh_total", start_afresh_total)
        print("running_total before adding nums[i]", running_total)
        running_total += nums[i]
        print("running_total after adding nums[i]", running_total)
        best_running_total = max(start_afresh_total, running_total)
        print("best_running_total", best_running_total)
        best_seen_total = max(best_running_total, best_seen_total)
        print("best_seen_total", best_seen_total)

        running_total = best_running_total

        i += 1
    
    return best_seen_total

# debug your code below
# print(max_subarray_sum([-1, 2, -3, 4]))
print(max_subarray_sum([2, 3, -2, 4] ))