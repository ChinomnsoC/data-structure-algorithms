def romanToInt(s):
    
    # Replace this placeholder return statement with your code
    # first create a dictionary for the roman numerals, "symbol": value
    # running_sum = 0
    # for character in string, validate that the value of char symbol is greater than the value
    # of char + 1 symbol. if so, update running_sum with value of char in dictionary
    # move i one step. if not, update running_sum with char + i value - char value
    numerals_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    running_sum = 0
    i = 0
    
    while i < len(s):
        print("i", i)
        value_of_i = numerals_map[s[i]]
        if i + 1 < len(s):
            value_of_i_plus_one = numerals_map[s[i+1]]
            if value_of_i >= value_of_i_plus_one:
                running_sum += value_of_i
                i += 1
                print("running_sum in if", running_sum)
                
            else:
                print("s, i and s i plus 1", s[i], s[i+1])
                difference = value_of_i_plus_one - value_of_i
                running_sum += difference
                i += 2
                print("less than length i", i)
                print("running_sum", running_sum)
        else:
            print("last else i", i)
            running_sum += value_of_i
            i += 1
        
    return running_sum