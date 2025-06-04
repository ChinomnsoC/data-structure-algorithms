def find_closest_elements(nums, k, target):
    n = len(nums)
    if n == k:
        return nums
    #  If the target is smaller than the smallest
    #  element or larger than the largest, return either the first or last k elements.
    if target < nums[0]:
        print(nums[:k])
        return nums[:k]
    elif target > nums[n - 1]:
        print(nums[k - 1 :])
        return nums[len(nums)-k : len(nums)]

    # If the length of nums is exactly k, return the entire list. If the target is smaller than the smallest element or larger than the largest, return either the first or last k elements.
    # Use binary search to locate the index of the element closest to the target.
    # Initialize the left and right bounds around the closest index.
    # Gradually expand the window by comparing distances from the target to elements on the left and right until it contains k elements.
    # Return the subarray within the final window bounds.
    first_closest = binary_search(nums, target)
    print(first_closest)
    window_left = first_closest - 1
    window_right = window_left + 1
    while (window_right - window_left - 1) < k:
        if window_left == -1:
            window_right += 1
            continue

        if window_right == len(nums) or abs(nums[window_left] - target) <= abs(
            nums[window_right] - target
        ):
            window_left -= 1

        else:
            window_right += 1

    return nums[window_left + 1 : window_right]


def binary_search(array, target):
    n = len(array) - 1
    left, right = 0, n
    while left <= right:
        midi_position = (left + right) // 2
        if array[midi_position] == target:
            return midi_position
        elif array[midi_position] < target:
            left = midi_position + 1
        else:
            right = midi_position - 1
    return left


number = [1, 2, 3, 4, 5, 6, 7]
print(find_closest_elements(number, 5, 7))
