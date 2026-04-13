class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}
        
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if char_map[char] == 1:
                return i
        
        return -1