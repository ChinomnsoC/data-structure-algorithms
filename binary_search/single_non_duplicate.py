# You are given a sorted array where every element appears exactly twice, except for one element which appears only once. 
# Find that single element. Must be O(log n) time.
def single_non_duplicate(nums: list) -> int:
    
    if len(nums) == 1:
        return nums[0]
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if mid % 2 == 1:
            mid -= 1
            
        
        if nums[mid] == nums[mid + 1]:
            # single element is to the right
            left = mid + 2
        else:
            # to the left
            right = mid
    
    return nums[left]

def do_tests_pass() -> bool:
    assert single_non_duplicate([1,1,2,3,3,4,4,8,8]) == 2
    assert single_non_duplicate([3,3,7,7,10,11,11]) == 10
    assert single_non_duplicate([1]) == 1
    assert single_non_duplicate([1,1,2]) == 2
    assert single_non_duplicate([1,2,2]) == 1
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")