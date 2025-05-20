def findRepeatedDnaSequences(s):
    length_of_string = len(s)
    if length_of_string < 10:
        return []
    
    seen_sequence = set()
    duplicates = set()
    
    for i in range(length_of_string - 9):
        window = s[i:i+10]
        if window in seen_sequence :
            duplicates.add(window)
        else:
            seen_sequence.add(window)
    print(list(duplicates))
    return list(duplicates)

# The method below is not as optimal as the one above
# def findRepeatedDnaSequences(s):
#     list_of_strings = []
#     length_of_string = len(s)
#     if length_of_string < 10:
#         return s
    
#     window_result = [s[0:10]]
#     print(window_result)
    
#     for i in range(len(s) - 9):
#         # print(i)
#         window = s[i+1:i+11]
#         print(window)
#         if window in window_result and window not in list_of_strings:
#             list_of_strings.append(window)
#             window = s[i+1:i+10]
#         else:
#             window_result.append(window)
#             window = s[i+1:i+10]
#     print(list_of_strings, window_result)
#     return list_of_strings
    

sample = "ACGTACGTACGGGTTACGTACGTAC"
findRepeatedDnaSequences(sample)