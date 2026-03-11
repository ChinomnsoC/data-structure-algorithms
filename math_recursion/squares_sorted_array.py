def sorted_squares(nums: list) -> list:
    if not nums:
        return []
    
    sorted_nums = []
    left, right = 0, len(nums) -1
    
    while left <= right:
        square_left = nums[left] * nums[left]
        square_right = nums[right] * nums[right]
        
        max_square = max(square_left, square_right)
        print(max_square)
        
        sorted_nums.append(max_square)
        
        if square_left >= square_right:
            left += 1
        else:
            right -= 1

    return sorted_nums[::-1]

def do_tests_pass() -> bool:
    assert sorted_squares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sorted_squares([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert sorted_squares([0]) == [0]
    assert sorted_squares([-1]) == [1]
    assert sorted_squares([1,2,3]) == [1,4,9]
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")