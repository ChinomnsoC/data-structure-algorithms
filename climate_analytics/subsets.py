# Given an integer array of unique elements, return all possible subsets (the power set).
# The solution must not contain duplicate subsets.
# Input: [1,2,3]
# Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

def subsets(input):
    n = len(input)
    output = []
    solution = []
    
    def backtracking(i):
        if i == n:
            output.append(solution[:])
            return
        
        # don't pick
        backtracking(i + 1)
        
        # pick
        solution.append(input[i])
        backtracking(i + 1)
        solution.pop()
    
    backtracking(0)
    return output

print(subsets([1, 2, 3]))
print(subsets([1]))
print(subsets([-4, 5, 9, 10]))
print(subsets([]))
    