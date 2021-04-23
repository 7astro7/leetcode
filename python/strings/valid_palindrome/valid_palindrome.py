
"""
Given a string s, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""

class Solution:

    def is_palindrome(
            self,
            s: str,
            ) -> bool:
        simplify = lambda char: char.isalnum()
        new_str = "".join(tuple(filter(simplify, s.lower())))
        return new_str[::-1] == new_str
