class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}

        for i in range(len(s)):

            curr_char = s[i]
            print(curr_char)

            if curr_char not in char_map:
                char_map[curr_char] = [i, 1]
            
            else:
                char_map[curr_char][1] += 1
        print(char_map)
        for position, freq in char_map.values():
            if freq == 1:
                return position
        
        return -1