def longest_palindrome(s: str) -> str:
    
    start, max_len = 0, 1
    
    for i in range(len(s)):
        
        for j in range(2):
            left, right = i, i+j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    start = left
                    max_len = current_len
                    
                left -= 1
                right += 1
        
    return s[start:start + max_len]
            

def do_tests_pass() -> bool:
    assert longest_palindrome("babad") in ["bab", "aba"]  # both valid
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ["a", "c"]
    assert longest_palindrome("racecar") == "racecar"
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")