
"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
"""

class Solution:

    def plus_one(self, digits: list) -> list:
        as_str_arr = '-'.join(str(i) for i in digits).split('-')
        as_str_arr = list(str(int(''.join(as_str_arr)) + 1))
        return list(int(i) for i in as_str_arr)


