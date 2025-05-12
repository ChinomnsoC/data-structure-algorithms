## General template for hare and tortoise

```python
FUNCTION fastAndSlow(dataStructure):
  # initialize pointers (or indices)
  fastPointer = dataStructure.start   # or 0 if the data structure is an array
  slowPointer = dataStructure.start   # or 0 if the data structure is an array
  
  WHILE fastPointer != null AND fastPointer.next != null: 
    # For arrays: WHILE fastPointer < dataStructure.length AND (fastPointer + 1) < dataStructure.length:
    
    slowPointer = slowPointer.next            
    # For arrays: slowPointer = slowPointer + 1
    
    fastPointer = fastPointer.next.next       
    # For arrays: fastPointer = fastPointer + 2
    
    IF fastPointer != null AND someCondition(fastPointer, slowPointer):
      # For arrays: use someCondition(dataStructure[fastPointer], dataStructure[slowPointer]) if needed
      handleCondition(fastPointer, slowPointer)
      BREAK

  # process the result
  processResult(slowPointer)
  # For arrays: processResult(slowPointer) might process dataStructure[slowPointer]
```

## Problem: Circular Array Loop

## Statement

There is a circular list of non-zero integers called nums. Each number in the list tells you how many steps to move forward or backward from your current position:

- If nums[i] is positive, move nums[i] steps forward.
- If nums[i] is negative, move nums[i] steps backward.

As the list is circular:

- Moving forward from the last element takes you back to the first element.
- Moving backward from the first element takes you to the last element.

A cycle in this list means:

- You keep moving according to the numbers, and you end up repeating a sequence of indexes.
- All numbers in the cycle have the same sign (either all positive or all negative).
- The cycle length is greater than 1 (it involves at least two indexes).

Return true if such a cycle exists in the list or false otherwise.

Constraints:

- 1 ≤ nums.length ≤ 10^3
- -5000 ≤ nums[i] ≤ 5000
- nums[i] != 0