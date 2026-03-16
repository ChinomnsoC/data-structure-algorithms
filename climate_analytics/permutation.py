# Permutation.

# Given an array of distinct integers, return all possible permutations.
# Input: [1, 2, 3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

def permute_array(input_list):
    # initialize two empty arrays
    output_list = []
    
    solution = []
    
    def backtracking(solution, remaining):
        if not remaining:
            output_list.append(solution[:])
            return
        
        for i in range(len(remaining)):
            solution.append(remaining[i])
            backtracking(solution, remaining[:i] + remaining[i+1:])
            solution.pop()
    
    backtracking(solution, input_list)
    
    return output_list

print(permute_array([1, 2, 3]))
print(permute_array([1]))
print(permute_array([-4, 5, 9, 10]))
print(permute_array([]))