# Modified Binary Search

## Problem: Binary Search

Try to solve the Binary Search problem.

We are given an array of integers, nums, sorted in ascending order, and an integer value, target. If the target exists in the array, return its index. If the target does not exist, return -1.

Constraints:

- 1 ≤ nums.length ≤ 10^3
- -10^4 ≤ nums[i], target ≤ 10^4
- All integers in nums are unique.
- nums is sorted in ascending order.

## Problem: Search in Rotated Sorted Array

Try to solve the Search in Rotated Sorted Array problem.

You are given a sorted integer array, nums, and an integer, target. The array may have been rotated by an arbitrary number. Your task is to find and return the index of target in this array. If target does not exist, return -1.

An original sorted array before rotation is given below:
![image](./Screenshot%202025-06-04%20at%2014.10.58.png)

Constraints:

- All values in nums are unique.
- The values in nums are sorted in ascending order.
- The array may have been rotated by some arbitrary number.
- 1 ≤ nums.length ≤ 1000
- -10^4 ≤ nums[i] ≤ 10^4
- -10^4 ≤ target ≤ 10^4


## Problem: Find K Closest Elements

You are given a sorted array of integers, nums, and two integers, target and k. Your task is to return k number of integers that are close to the target value, target. The integers in the output array should be in a sorted order.

An integer, nums[i], is considered to be closer to target, as compared to nums[j] when `(nums[i] - target) < nums[j] - target`. However, when `(nums[i] - target) = (nums[j] - target)`, the smaller of the two values is selected.

Constraints:

- 1 ≤ k ≤ nums.length
- 1 ≤ nums.length ≤ 10^3
- nums is sorted in ascending order.
- -10^4 ≤ nums[i], target ≤ 10^4