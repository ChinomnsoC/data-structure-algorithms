def eliminate_substring(s: str) -> str:
    target = "AWS"
    
    stack = []
    
    for char in s:
        stack.append(char)
        
        if stack[-3:] == ['A', 'W', 'S']:
            stack.pop(); stack.pop(); stack.pop()
    
    result = "".join(stack)
    
    return result if result else "-1"

def eliminate_substring_variation(s: str, target: str) -> str:
    
    stack = []
    tgt_length = len(target)
    
    for char in s:
        stack.append(char)
        
        if stack[-tgt_length:] == list(target):
            # call stack.pop tgt_length number of times
            for _ in range(tgt_length):
                stack.pop()
    result = "".join(stack)
    
    return result if result else "-1"

def do_tests_pass() -> bool:
    assert eliminate_substring("AWAWSSG") == "G"
    assert eliminate_substring("AWAWSS") == "-1"
    assert eliminate_substring("AWS") == "-1"
    assert eliminate_substring("AWSAWS") == "-1"
    assert eliminate_substring("HELLO") == "HELLO"
    assert eliminate_substring("") == "-1"
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")