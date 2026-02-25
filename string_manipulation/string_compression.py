# # Given an array of characters, compress it in-place so that consecutive repeated characters are replaced by the character followed by its count. If the count is 1, don't write the count. Return the new length.

# Examples:
# ["a","a","b","b","c","c","c"] → ["a","2","b","2","c","3"], return 6
# ["a"] → ["a"], return 1
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"] → ["a","b","1","2"], return 4
# Key constraint: in-place — modify the original array, don't create a new one.


def compress(chars: list) -> int:
    length_of_chars = len(chars)

    left, right = 0, 0
    write = 0

    # loop through the string,
    # compare value at left position with value at right position.
    # if they are thesame, move right by one place forward
    # increase counter by 1
    # keep doing this until the value of right is != value of left
    # when this happens, move left to be in right minus 1.
    # then update the value of current left to be the vlaue of the counter, as a string
    # update super counter to be += counter
    # reset counter to zero.
    # reset left and right to be the same position
    # repeat
    # return super counter

    
    # ["a","a","a","b","b","c","6","c"]
    
    while left < length_of_chars:
        
        current_char = chars[left]
        right = left
        
        counter = 0
        
        while right < length_of_chars and chars[right] == current_char:
            right += 1
            counter += 1
        
        print(write)
        chars[write] = current_char
        write += 1
        
        if counter > 1:
            for i in str(counter):
                chars[write] = i
                write += 1
        left = right
    return write
        


def do_tests_pass() -> bool:
    test1 = ["a", "a", "b", "b", "c", "c", "c"]

    result = compress(test1)
    assert result == 6 and test1[:6] == ["a", "2", "b", "2", "c", "3"]

    test2 = ["a"]
    assert compress(test2) == 1 and test2[:1] == ["a"]

    test3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert compress(test3) == 4 and test3[:4] == ["a", "b", "1", "2"]

    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
