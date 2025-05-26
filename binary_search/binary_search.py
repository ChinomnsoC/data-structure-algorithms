def binary_search(nums, target):
    n = len(nums)
    if n == 1 and target == nums[0]:
        return 0
    elif n == 1 and target != nums[0]:
        return -1
    left, right = 0, n-1
    while left < right:
        midi_position = left + (right - left) // 2
        if nums[midi_position] == target:
            return midi_position
        elif nums[midi_position] > target:
            left, right = left, midi_position - 1
            if left == right and nums[left] == target:
                return left
        else:
            left, right = midi_position+1, right
            if left == right and nums[left] == target:
                return left
    return -1
odd_list = [5,6,7,8,9]
even_list = [2,3,4,5]

binary_search(odd_list, 10)
binary_search(even_list, 5)
