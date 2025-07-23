# Follow this please:
# * Initialize two pointers at the end of the string.
# * Move left pointer to skip spaces.
# * Mark word end, move left until a space/start is found.
# * Extract substring (word), add to result.
# * Repeat until start of string.

def reverse_words(sentence):
    if not sentence:
        return ""
    
    n = len(sentence)
    left = n -1
    right = n - 1
    result = []
    
    while left >=0:
        while left >= 0 and sentence[left] == " ":
            left -= 1
        
        if left < 0:
            break
        
        right = left
        
        while left >= 0 and sentence[left] != ' ':
            left -= 1
        
        word = sentence[left + 1:right + 1]
        result.append(word)
    
    return ' '.join(result)
        
# Test the solutions
def test_reverse_words():
    test_cases = [
        " hello world! ",
        "  multiple   spaces  between  words  ",
        "single",
        "a b c",
        "   leading and trailing   ",
        "123 abc XYZ"
    ]
    
    print("Testing reverse_words (two-pointer approach):")
    for test in test_cases:
        result = reverse_words(test)
        print(f"Input: '{test}' -> Output: '{result}'")
    

# Run tests
if __name__ == "__main__":
    test_reverse_words()