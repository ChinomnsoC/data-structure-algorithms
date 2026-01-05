def ThreeNumbers(strParam):
    param_list = strParam.split()


    for word in param_list:
        unique_int = []
        for i in range(len(word)):
            left = i + 1
            right = left + 1
            if word[i].isdigit() and word[i] not in unique_int:
                if left < len(word) and right < len(word):
                    if word[left].isdigit() and word[right].isdigit():
                        return "false"
                unique_int.append(word[i])
        if len(unique_int) != 3:
            # print(f"there are {len(unique_int)} unique integers {unique_int} in this word {word}")
            return "false"
    return "true"


# keep this function call here
# print(ThreeNumbers(input()))


def check_is_unique_digit(word):
    unique_int = []
    for char in word:
        if char.isdigit() and char not in unique_int:
            unique_int.append(char)

    if len(unique_int) != 3:
        print(f"there are {len(unique_int)} unique integers in this word {word}")
        return False


# def check_is_unique_digit_not_adjacent(word):
#     unique_int = []
#     character_index_map = {}
#     for right in range(len(word)):
#         char = word[right]
#         if char.isdigit() and char not in character_index_map:
#             character_index_map[word[right]] += 1
#             right += 1

#     if len(unique_int) != 3:
#         print(f"there are {len(unique_int)} unique integers in this word {word}")
#         return False


# keep this function call here
print(ThreeNumbers("2a3b5 w1o2rl3d g1gg92"))
print(ThreeNumbers("21aa3a ggg4g4g6ggg"))
print(ThreeNumbers("a1b1c2"))