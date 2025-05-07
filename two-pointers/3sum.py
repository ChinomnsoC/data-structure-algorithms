def three_sum(nums):
  nums.sort()
  target = 0
  length_of_nums = len(nums)
  triplets = []
    

  for i in range(length_of_nums - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    
    left_pointer = i + 1
    right_pointer = length_of_nums - 1
    print("left pointer, right pointer", nums[left_pointer], nums[right_pointer], nums[i])
    
    while left_pointer < right_pointer:
      total = nums[i] + nums[left_pointer] + nums[right_pointer]
      print("total", total)
      if total == target:
        print(" in the loop total zero left pointer, right pointer", nums[left_pointer], nums[right_pointer], nums[i])
        triplets.append([nums[i], nums[left_pointer], nums[right_pointer]])
        left_pointer += 1
        right_pointer -= 1
        print(" in the loop after moving left pointer, right pointer", nums[left_pointer], nums[right_pointer], nums[i])
        
        while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
            left_pointer += 1
        while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
            right_pointer -= 1
      elif total < 0:
          left_pointer += 1
      else:
          right_pointer -= 1

  return triplets


# --------------------------
# Example usage
# --------------------------

our_list = [-3,-2,-1,0,1,2,3]
test_cases = [
        # Test Case 1: Basic case
        [-1, 0, 1, 2, -1, -4],
        # Test Case 2: No valid triplets
        [1, 2, 3, 4, 5],
        # Test Case 3: All zeros
        [0, 0, 0, 0],
        # Test Case 4: Mixed numbers with duplicates
        [-4, -1, -1, 0, 1, 2, 2],
        # Test Case 5: Large negative and positive range
        [-10, -7, -3, -1, 0, 3, 7, 10],
        # Test Case 6: All negative
        [-3, -5, -7, -9]
    ]

