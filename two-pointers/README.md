## Statement

Given a string, s, return TRUE if it is a palindrome; otherwise, return FALSE.

A phrase is considered a palindrome if it reads the same backward as forward after converting all uppercase letters to lowercase and removing any characters that are not letters or numbers. Only alphanumeric characters (letters and digits) are taken into account.

Constraints:

1
≤
1≤
 s.length 
≤
3000
≤3000

s consists only of printable ASCII characters.

## Problem: 3Sum

Given an integer array nums, find and return all unique triplets [nums[i], nums[j], nums[k]], where the indexes satisfy i ≠

=
j, i
≠

=
k, and j
≠

=
k, and the sum of the elements nums[i] + nums[j] + nums[k] == 0.

Constraints:

- 3≤ nums.length ≤ 500
- -10 ≤ nums[i] ≤ 10^3

## Problem: Sort Colors

Statement
Given an array, colors, which contains a combination of the following three elements:

- 0 (representing red)
- 1 (representing white)
- 2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue. To improve your problem-solving skills, do not utilize the built-in sort function.

Constraints:

- 1 ≤ colors.length ≤ 300
- colors[i] can only contain 0s, 1s, or 2s.

Example:
![image](./Screenshot%2025-05-07%at%08.06.34.png)

## Problem: Maximum Array of a Contiguous Subarray

Given an array of integers nums, and an integer k, return the maximum average of a contiguous subarray of length k.

Constraints:
1 ≤ k ≤ nums.length ≤ 10^5
-10^4 ≤ nums[i] ≤ 10^4

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Expected Output: 12.75
Explanation: The subarray [12,-5,-6,50] has the maximum average of 12.75.

Please implement a Python method to solve this problem.

## Problem: Sort Colors


You are given a string, sentence, comprising words and leading or trailing spaces or multiple spaces between words. Your task is to reverse the order of its words without affecting the order of letters within the given word. Return the modified sentence.
Note: A word is defined as a continuous sequence of non-space characters. Multiple words separated by single spaces form a valid English sentence. Therefore, ensure there is only a single space between any two words in the returned string, with no leading, trailing, or extra spaces.
Constraints:

* The sentence contains English uppercase and lowercase letters, digits, and spaces.
* There is at least one word in sentence.
* 1 ≤ sentence.length ≤ 10^4
Example: Input: " hello world! " Expected Output: “world! hello”
Please implement your solution in Python.