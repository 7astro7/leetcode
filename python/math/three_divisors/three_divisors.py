
"""
Given an integer n, return true if n has exactly three positive 
divisors. Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that 
n = k * m.

Example 1:
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.

Constraints:
    1 <= n <= 1e4
"""

class Solution:

    def is_three(self, n: int) -> bool:
        divisor_count = 1 # 1 is a divisor
        i = 2
        while True:
            if i > n:
                return divisor_count == 3
            if not n % i:
                divisor_count += 1
            i += 1


