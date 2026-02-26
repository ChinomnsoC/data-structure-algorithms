def find_subsequences(dictionary: list, input_str: str) -> list:
    if not dictionary or not input_str:
        return []
    final = []
    for word in dictionary:
        if is_subsequence(word, input_str):
            final.append(word)
    
    return final
            

def is_subsequence(word, input_str) -> bool:
    
    i, j = 0, 0
    
    while i < len(word) and j < len(input_str):
        current_letter = word[i]
        if input_str[j] == current_letter:
            i += 1
            j += 1
        else:
            j += 1
    
    if i == len(word):
        return True
    
    return False

                    
                    
        # find out if j > last seen
        # if j > last seen and i == len(word) -1
        # then we've seen all the letters and is_subsequence
        

def do_tests_pass() -> bool:
    dictionary = ["cat", "at", "cot", "catch"]
    input_str = "yccuajhtxc"
    
    
    result = find_subsequences(dictionary, input_str)
    assert sorted(result) == sorted(["cat", "at"])
    
    # empty input
    assert find_subsequences(["cat"], "") == []
    
    # empty dictionary
    assert find_subsequences([], "yccuajhtxc") == []
    
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")