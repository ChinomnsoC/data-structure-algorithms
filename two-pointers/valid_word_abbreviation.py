def valid_word_abbreviation(word, abbr):
    print(f"Checking: word='{word}', abbr='{abbr}'")
    left_word, left_abbr = 0, 0

    while left_abbr < len(abbr) and left_word < len(word):
        # handle numbers
        if abbr[left_abbr].isdigit():
                if abbr[left_abbr] == '0':
                    return False
                
                num_str = ""
                
                while left_abbr < len(abbr) and abbr[left_abbr].isdigit():
                    num_str += abbr[left_abbr]
                    print("num_str", num_str)
                    left_abbr += 1
            
                num = int(num_str)
                left_word += num
        
        # handle letters
        else:
            if left_word >= len(word):
                return False
            if abbr[left_abbr] != word[left_word]:
                return False
                print("abbr[left_abbr] == word[left_word]", abbr[left_abbr], word[left_word])
            left_word += 1
            left_abbr += 1
                
    result = left_word == len(word) and left_abbr == len(abbr)   
    return result
