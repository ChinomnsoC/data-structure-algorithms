# A string is valid if all characters appear the same number of times, 
# OR if removing exactly one character makes all remaining characters appear the same number of times.

# "aaabbb"         → True   (a:3, b:3 — already equal)
# "aaabbbcccc"     → True   (remove one c → a:3, b:3, c:3)
# "aaabbbccccdddd" → False  (need to remove 2)
# "aabbcccdddeeee" → False


def cool_string(s):
    if not s or not s.isalpha():
        return False
    
    s_freq_map = {}
    
    for char in s:
        s_freq_map[char] = s_freq_map.get(char, 0) + 1
        
    print(s_freq_map)
    counts_freq_values = list(s_freq_map.values())
    max_freq = max(s_freq_map.values())
    min_freq = min(s_freq_map.values())
    diff_freq =  max_freq - min_freq
    
    if diff_freq == 0:
        return True
    
    if diff_freq == 1:
        # only one char has the max 
        if counts_freq_values.count(max_freq) == 1:
            return True
            
        # only one char is at min
        if counts_freq_values.count(min_freq) == 1:
            return True
    
    if max_freq == 1:
        return True
    
    # one char appears once, but the rest are equal.
    if counts_freq_values.count(1) == 1 and len(set(counts_freq_values) - {1} ) == 1:
        return True
    
    return False

print(cool_string("aaabbb")) # → True   (a:3, b:3 — already equal)
print(cool_string("aaabbbcccc")) # → True   (remove one c → a:3, b:3, c:3)
print(cool_string("aaabbbccccdddd")) # → False  (need to remove 2)
print(cool_string("aabbcccdddeeee")) # → False
print(cool_string("abbbcccdddeee"))