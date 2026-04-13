
def groupAnagrams(strs):
    
    anagrams_map = {}
    
    for word in strs:
        count_key = [0] * 26
        
        for char in word:
            index = ord(char) - ord('a')
            count_key[index] += 1
            
        key = tuple(count_key)
        
        if key not in anagrams_map:
            anagrams_map[key] = []
        
        anagrams_map[key].append(word)
    
    
    return list(anagrams_map.values())
