# **Generate Parentheses (LC 22)**

# Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

# ```
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Input: n = 1
# Output: ["()"]
# ```

# You discussed the approach — backtracking with open/close counts. Code it.


def generate_parenthesis(n):
    if not n:
        return []
    
    formed = []
    
    def backtrack(open_bracket_count, closed_bracket_count, current_string):
        if open_bracket_count == n and closed_bracket_count == n:
            formed.append(current_string)
            return
        
        if open_bracket_count < n:
            backtrack(open_bracket_count + 1, closed_bracket_count, current_string + "(")
        
        if closed_bracket_count < open_bracket_count:
            backtrack(open_bracket_count, closed_bracket_count + 1, current_string + ")")
    
    backtrack(0, 0, "")
    return formed


print(generate_parenthesis(3))