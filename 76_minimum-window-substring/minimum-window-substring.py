from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        s_count, t_count = Counter, Counter(t)
        
        left_side, right_side = 0, 0
        
        