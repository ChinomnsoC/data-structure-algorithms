from collections import Counter


def single_non_duplicate(nums):
    answer = Counter(nums)
    last_single = [key for key, val in answer.items() if val == 1][-1]
    print(answer)
    return last_single

number = [0,0,1,1,2,2,4,8,8,16,16,32,32]
print(single_non_duplicate(number))