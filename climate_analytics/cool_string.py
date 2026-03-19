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
    max_freq = max(s_freq_map.values())
    diff_freq =  max_freq - min(s_freq_map.values())
    
    if diff_freq <= 1:
        if diff_freq == 0:
            return True
        count_max_char = 0
        for char, count in s_freq_map.items():
            if count == max_freq:
                count_max_char += 1
                
        if count_max_char == 1:
            return True
        else:
            return False
    
    else: 
        return False
        

print(cool_string("aaabbb")) # → True   (a:3, b:3 — already equal)
print(cool_string("aaabbbcccc")) # → True   (remove one c → a:3, b:3, c:3)
print(cool_string("aaabbbccccdddd")) # → False  (need to remove 2)
print(cool_string("aabbcccdddeeee")) # → False