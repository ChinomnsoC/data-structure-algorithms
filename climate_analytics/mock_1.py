# Problem 1:
# Given a list of intervals where intervals[i] = [start, end], 
# merge all overlapping intervals and return an array of the non-overlapping intervals.
# Input:  [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# Input:  [[1,4],[4,5]]
# Output: [[1,5]]
def merge_intervals(intervals):
    
    if not intervals:
        return 
    intervals.sort(key=lambda x:(x[0]))
    
    output = [intervals[0]]
    
    for interval in intervals[1:]:
        print(interval[0])
        print(output[-1][1])
        if interval[0] <= output[-1][1]:
            # we have an overlap
            merged = merge(interval, output[-1])
            
            output[-1] = merged
        
        else:
            output.append(interval)
            
        
        
    return output


def merge(input, output):
    
    merged = [min(input[0], output[0]), max(input[1], output[1])]
    return merged


print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

# Problem 2:
# Given a string s and a string t, return the minimum window substring of s such 
# that every character in t (including duplicates) is included in the window. If there is no such substring, 
# return an empty string.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Input: s = "a", t = "a"  
# Output: "a"

# Input: s = "a", t = "aa"
# Output: ""


def min_window_substring(s, t):
    t_map = {}
    
    have_map = {}
    
    for char in t:
        t_map[char] = t_map.get(char, 0) + 1
        
    required_length = len(t_map)
    
    min_length = float('inf')
    min_start = 0
    
    left, right, formed = 0, 0, 0
    
    for right in range(len(s)):
        curr_char = s[right]
        
        if curr_char in t_map:
            have_map[curr_char] = have_map.get(curr_char, 0) + 1
            
            curr_char_have = have_map[curr_char]
            if curr_char_have == t_map[curr_char]:
                formed += 1
    
        while formed == required_length:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left
            
            left_char = s[left]
            if left_char in have_map:
                have_map[left_char] -= 1
                
                if left_char in t_map and have_map[left_char] < t_map[left_char]:
                    formed -= 1
                
            left += 1
        
    
    return s[min_start:min_start+min_length] if min_length != float('inf') else ""
        
print(min_window_substring("ADOBECODEBANC", "ABC"))