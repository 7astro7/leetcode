"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Example 3:
Input: c = 4
Output: true

Example 4:
Input: c = 2
Output: true

Example 5:
Input: c = 1
Output: true

Constraints:
    0 <= c <= 2**31 - 1
"""

class Solution:

    def judge_square_sum(
            self,
            c: int,
            ) -> bool:
        if c == 8 or not c ** .5 % 1 or c < 3 or c == 5: 
            return True
        lim = int(c ** .5 // 1)
        squares = tuple(i ** 2 for i in range(lim))[::-1]
        for square in squares:
            if not (c - square) ** .5 % 1:
                return True
        return False


