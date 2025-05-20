def find_longest_substring(input_str):
    if len(set(input_str)) == 1: #if all characters are the same in the input list, return 1
        return 1
    if len(set(input_str)) == len(input_str):
        return len(input_str)
    character_index_map = {}
    left, right, max_frequency = 0, 0, 0
    
    
    for right in range(len(input_str)):
        char = input_str[right]
        if char in character_index_map and character_index_map[char] >= left:
            left = character_index_map[char] + 1
            
        character_index_map[char] = right
        max_frequency = max(max_frequency, right - left + 1)       
        
    print(max_frequency)
    return max_frequency

# from collections import defaultdict

# def find_longest_substring(input_str):
#     if len(set(input_str)) == 1: #if all characters are the same in the input list, return 1
#         return 1
#     if len(set(input_str)) == len(input_str):
#         return len(input_str)
    
#     character_index_map = defaultdict(int)
#     left, right, max_frequency = 0, 0, 0
    
#     for right in range(len(input_str)):
#         if input_str[right] not in character_index_map:
#             character_index_map[input_str[right]] += 1
#             max_frequency += 1
#             right += 1
            
#         if input_str[right] in character_index_map:
#             character_index_map[input_str[right]] += 1
#             left +=1 
#             right += 1
#         # For each character, if the hash map does not contain the current character, 
#         # store it with its index as the value.
#         # increase max max_frequency from 0 to 1
#         # then slide right by one space. If input_str[right] is not in character_index_map, 
#         # increase max_frequency by 1, slide right by one step again.
#         # If input_str[right] is in character_index_map, update character_index_map
#         # slight left by one step, slide right also
#         # return max_frequency
        
        
#     return max_frequency

# Example usage
# s1 = "abcdefg" 
# s2 = "aaaaaaa"
# s3 = "abcabcbb"
# s4 = "" 
# s5 = "bbbbbabcdef" 
sample = "bbbbbabcdef"
find_longest_substring(sample)
