# Given an integer array nums and an integer k, return the k most frequent elements regardless of order. It is guaranteed that the answer is unique.

# Follow up: Can the time complexity be better than O(n log n), where n is the array's size?

def most_freq_element(arr, k):
    freq_map = {}
    for i in range(len(arr)):
        if arr[i] not in freq_map:
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
        
        freq_map[arr[i]] += 1
    
    