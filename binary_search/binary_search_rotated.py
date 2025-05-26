def binary_search_rotated(nums, target):
  n = len(nums)
  left, right = 0, n-1
  
  while left <= right:
    mid = left + (right - left) // 2
    left_is_sorted = nums[left] <= nums[mid]
    right_is_sorted = nums[mid] <= nums[right]
    if nums[mid] == target:
      return mid
    elif left_is_sorted:
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    elif right_is_sorted:
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
    else:
      return -1

  return -1