import collections

def longest_palindrome(s):
    character_count_hash_map = collections.Counter(s)
    length_of_palindrome = 0
    
    for count in character_count_hash_map.values():
        length_of_palindrome += count // 2 * 2
    
    if length_of_palindrome < len(s):
        length_of_palindrome += 1
    
    return length_of_palindrome