# Candy Crush

# Write a function to crush candy in one dimensional board. 
# In candy crushing games, groups of like items are removed from the board. 
# In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. 
# This process should be repeated as many time as possible. 
# You should greedily remove characters from left to right.

# Example 1:

# Input: "aaabbbc"
# Output: "c"
# Explanation:
# 1. Remove 3 'a': "aaabbbbc" => "bbbbc"
# 2. Remove 4 'b': "bbbbc" => "c"
# Example 2:

# Input: "aabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aabbbacd" => "aaacd"
# 2. Remove 3 'a': "aaacd" => "cd"
# Example 3:

# Input: "aabbccd
# Explanation:
# 1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
# 2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
# 3. Remove 3 'c': "aabbcccba" => "aabbba"
# 4. Remove 3 'b': "aabbba" => "aaa"
# 5. Remove 3 'a': "aaa" => ""
# Example 4:

# Input: "aaabbbacd"
# Output: "acd"
# Explanation:
# 1. Remove 3 'a': "aaabbbacd" => "bbbacd"
# 2. Remove 3 'b': "bbbacd" => "acd"
# Followup: What if you need to find the shortest string after removal?

# Example:

# Input: "aaabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aaabbbacd" => "aaaacd"
# 2. Remove 4 'a': "aaaacd" => "cd"

# Time: O(n), Space: O(n)

def candy_crush(input):
    # [[]]
    stack = []
    
    for char in input:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        
        else:
            stack.append([char, 1])
        
        
        if stack[-1][1] >= 3:
            stack.pop()    
                
            
        
    # build string from stack 
    
    output = ''.join(char * count for char, count in stack)
        
        
    return output

print(candy_crush("aaabbbacd"))
print(candy_crush("aaabbbc"))           # expected "c"
print(candy_crush("aabbbacd"))          # expected "cd"
print(candy_crush("aabbccddeeedcba"))   # expected ""
print(candy_crush(""))