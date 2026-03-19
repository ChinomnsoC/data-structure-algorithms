# Valid Parenthesis
# Given a string containing just (, ), {, }, [, ], determine 
# if the input string is valid. Brackets must close in the correct order.
# "()"       → True
# "()[]{}"   → True
# "(]"       → False
# "([)]"     → False
# "{[]}"     → True

def valid_parenthesis(brackets_string):
    
    if not brackets_string:
        return False
    stack = []
    
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in brackets_string:
        if char in matching:
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return False if stack else True
    
    # opening = ["[", "(", "{"]
    # for char in brackets_string:
    #     if char in opening:
    #         stack.append(char)
    #     else:
    #         # if stack and last char in stack is the opening of char:
    #         if stack and stack[-1] == matching[char]:
    #             stack.pop()
    #         else:
    #             return False
    
    # return True

print(valid_parenthesis("{[]()}")) # -> True
print(valid_parenthesis("()"))  # → True
print(valid_parenthesis("()[]{}"))  # → True
print(valid_parenthesis("(]"))  # → False
print(valid_parenthesis("([)]"))  # → False
print(valid_parenthesis("{[]}"))  # → True
print(valid_parenthesis("{[](})")) # -> False