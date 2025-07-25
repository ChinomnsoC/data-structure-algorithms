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

## Problem: Maximum Average of a Contiguous Subarray

Given an array of integers nums, and an integer k, return the maximum average of a contiguous subarray of length k.

Constraints:
1 ≤ k ≤ nums.length ≤ 10^5
-10^4 ≤ nums[i] ≤ 10^4

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Expected Output: 12.75
Explanation: The subarray [12,-5,-6,50] has the maximum average of 12.75.

Please implement a Python method to solve this problem.

## Problem: Reverse words in a string

You are given a string, sentence, comprising words and leading or trailing spaces or multiple spaces between words. Your task is to reverse the order of its words without affecting the order of letters within the given word. Return the modified sentence.
Note: A word is defined as a continuous sequence of non-space characters. Multiple words separated by single spaces form a valid English sentence. Therefore, ensure there is only a single space between any two words in the returned string, with no leading, trailing, or extra spaces.
Constraints:

* The sentence contains English uppercase and lowercase letters, digits, and spaces.
* There is at least one word in sentence.
* 1 ≤ sentence.length ≤ 10^4
Example: Input: " hello world! " Expected Output: “world! hello”
Please implement your solution in Python.

## Problem: Max Number of Fruits

While visiting a farm of fruits, you are given a row of fruits represented by an integer array, fruits, where fruits[i] is the type of fruit the i-th tree produces.

You have to collect fruits, but you must follow these rules:

You are given only two baskets, each able to hold an unlimited quantity of one fruit type.
You can start collecting from any tree, but must collect exactly one fruit from each tree moving to the right.
You must stop once you encounter a tree whose fruit type cannot fit into your baskets.
Return the maximum number of fruits you can collect following these rules.

Constraints: 1 ≤ fruits.length ≤ 10³
0 ≤ fruits[i] < fruits.length

Examples:

Input: fruits = [1,2,1]
Output: 3
Explanation: Window [1,2,1] uses only fruit types 1 and 2.

Input: fruits = [0,1,2,2]
Output: 3
Explanation: Window [1,2,2] uses only fruit types 1 and 2.

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: Window [2,3,2,2] uses fruit types 2 and 3.

Please provide your Python solution for this problem.

## Valid Word Abbreviation

Try to solve the Valid Word Abbreviation problem.

Statement
Given a string, word, and abbreviation, abbr, return TRUE if the abbreviation matches the given string. Otherwise, return FALSE. An abbreviation can replace any non-adjacent, non-empty substrings of the original word with their lengths. Replacement lengths must not contain leading zeros.

A certain word, "calendar", can be abbreviated as follows:

- "cal3ar" ("cal + end [length = 3] + ar" skipping three characters "end" from the word "calendar" still matches the provided abbreviation)
- "c6r" ("c + alenda [length = 6] + r" skipping six characters "alenda" from the word "calendar" still matches the provided abbreviation)
- The word "internationalization" can also be abbreviated as "i18n" (the abbreviation comes from skipping 18 characters in "internationalization" leaving the first and last letters "i" and "n").

The following are not valid abbreviations:

- "c06r" (Has leading zeroes)
- "cale0ndar" (Replaces an empty string)
- "c24r" ("c al enda r" the replaced substrings are adjacent)

Constraints:

- 1 ≤ word.length ≤ 20
- The word consists of only lowercase English letters.
- 1 ≤ abbr.length ≤ 10
- abbr consists of lowercase English letters and digits.
- All the integers in abbr will fit in a 32–bit integer.