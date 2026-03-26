# Given a string and an integer k, return the length of the longest substring 
# that contains at most k distinct characters.

# When you exceed k distinct characters, you don't reset both pointers. 
# You shrink from the left one step at a time until you're back to k distinct characters. Right keeps moving forward.
# Use a HashMap to track character frequencies in the window — when a character's count drops to 0, remove it from the map. 
# The number of keys in the map = number of distinct characters.


def longest_substring_k_distinct(s: str, k: int) -> int:
    
    if len(set(s))< k or k == 0:
        return 0
    
    char_map = {}
    
    left, right = 0, 0

    max_len = 0

    for right in range(len(s)):
        # add s[right] to char_map
        char = s[right]
        char_map[char] = char_map.get(char, 0) + 1
        # while len(char_map) > k: shrink from left
        
        while len(char_map) > k:
            left_char = s[left]
            char_map[left_char] -= 1
            
            
            if char_map[left_char] == 0:
                del char_map[left_char]
            left += 1
        
        max_len = max(max_len, (right - left + 1))
            
        # update max_len
    return max_len

def do_tests_pass() -> bool:
    assert longest_substring_k_distinct("eceba", 2) == 3   # "ece"
    assert longest_substring_k_distinct("aa", 1) == 2      # "aa"
    assert longest_substring_k_distinct("abcadcacacaca", 3) == 11  # "cadcacacaca"
    assert longest_substring_k_distinct("", 2) == 0
    assert longest_substring_k_distinct("abc", 0) == 0
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")