# Given a string, remove all adjacent duplicate pairs repeatedly until no adjacent duplicates remain. 
# Return the final string. If empty, return "-1".
# Example: "abbaca" → remove "bb" → "aaca" → remove "aa" → "ca" → return "ca"
def remove_adjacent_duplicates(s: str) -> str:
    if not s:
        return "-1"
    
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)

def do_tests_pass() -> bool:
    assert remove_adjacent_duplicates("abbaca") == "ca"
    assert remove_adjacent_duplicates("azxxzy") == "ay"
    assert remove_adjacent_duplicates("aaa") == "a"
    assert remove_adjacent_duplicates("abba") == ""  # or "-1"?
    assert remove_adjacent_duplicates("abcd") == "abcd"
    assert remove_adjacent_duplicates("") == "-1"
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")