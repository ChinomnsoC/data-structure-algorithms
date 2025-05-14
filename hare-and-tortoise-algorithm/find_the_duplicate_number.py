# def find_duplicate(nums):
#     seen = set()
#     slow = 0
#     fast = len(nums) - 1

#     while slow < len(nums) and fast >= 0:
#         # Compare nums[slow] and nums[fast]
#         if nums[slow] == nums[fast] and slow != fast:
#             return nums[slow]

#         # Check for duplicates in seen set
#         if nums[slow] in seen:
#             return nums[slow]
#         if nums[fast] in seen:
#             return nums[fast]

#         # Add current values to the set
#         seen.add(nums[slow])
#         seen.add(nums[fast])

#         # Move pointers
#         slow += 1
#         fast -= 1

#     return -1  # If no duplicate found (shouldn't happen per problem constraints)


def find_duplicates(nums):
    slow_pointer = nums[0]
    fast_pointer = nums[0]
    
    while True:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[nums[fast_pointer]]
        
        if slow_pointer == fast_pointer:
            break
        
    slow_pointer = nums[0]
    fast_pointer = fast_pointer
    
    while slow_pointer != fast_pointer:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[fast_pointer]

    return fast_pointer
sample = [3,4,3,1,2]
find_duplicates(sample)