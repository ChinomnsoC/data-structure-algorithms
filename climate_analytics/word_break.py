# **Word Break (LC 139)**

# Given a string `s` and a list of strings `wordDict`, return `True` if `s` 
# can be segmented into one or more dictionary words.

# ```
# s = "leetcode", wordDict = ["leet","code"]
# Output: True  # "leet" + "code"

# s = "applepenapple", wordDict = ["apple","pen"]
# Output: True  # "apple" + "pen" + "apple"

# s = "catsandog", wordDict = ["cats","and","dog","cat","san"]
# Output: False
# ```

def word_break(s, wordDict):
    word_dict_set = set(wordDict)
    n = len(s)
    
    dp = [False] * (n + 1)
    
    dp[0] = True
    
    
    for i in range(1, n+1):
        for j in range(0, i):
            if dp[j] == True and s[j:i] in word_dict_set:
                dp[i] = True
                break
    
    return dp[n]


s = "catsandog"
wordDict = ["cats","and","dog","cat","san"]

print(word_break(s, wordDict))

# Complexity: O(n²) time, O(n) space.