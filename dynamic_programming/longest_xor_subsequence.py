# Given an array of integers and an integer k, find the length of the longest subsequence 
# where each pair of adjacent elements has a bitwise XOR equal to k. 
# A subsequence of length 1 is always valid.

def longest_xor_subsequence(arr: list, k: int) -> int:
    
    len_longest_subsequence = 0
    
    n = len(arr)
    
    dp= [1] * n
    
    dp[0] = 1
    
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if (arr[i] ^ arr[j] )== k:
                dp[i] = max(dp[i], dp[j] + 1)
    
    
        len_longest_subsequence = max(len_longest_subsequence, dp[i])
        
    
    return max(dp)
    

def do_tests_pass() -> bool:
    assert longest_xor_subsequence([2, 1, 3, 5, 2], 2) == 2  # [1, 3]
    assert longest_xor_subsequence([1], 2) == 1               # single element
    assert longest_xor_subsequence([1, 2, 3], 0) == 1         # no valid pairs
    assert longest_xor_subsequence([1, 3, 1, 3, 1], 2) == 5  # entire array
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")