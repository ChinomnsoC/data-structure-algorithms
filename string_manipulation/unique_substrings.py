def unique_substrings(word: str, k: int):
    if not word:
        return 0
    
    left, right = 0, k
    
    substring_set = set()
    
    while right <= len(word):
        window = word[left:right]
        
        if window not in substring_set:
            substring_set.add(window)
            print(window)
            left += 1
            right += 1
        else:
            left += 1
            right += 1
    
    return len(substring_set)


def do_tests_pass() -> bool:
    assert unique_substrings("abcabc", 2) == 3
    assert unique_substrings("aaaa", 2) == 1
    assert unique_substrings("abcd", 2) == 3
    assert unique_substrings("", 2) == 0
    assert unique_substrings("abcd", 5) == 0  # k > len(s)
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")