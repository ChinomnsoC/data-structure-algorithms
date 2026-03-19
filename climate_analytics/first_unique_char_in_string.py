class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}

        for i in range(len(s)):

            curr_char = s[i]

            if curr_char not in char_map:
                char_map[curr_char] = [i, 1]
            
            count = char_map[curr_char][1]
            count += 1
        
        for key, value in char_map:
            if value[1] == 1:
                return index
        
        return -1