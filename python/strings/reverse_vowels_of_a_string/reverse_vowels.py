
"""
Given a string s, reverse only all the vowels in the string and 
return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in 
both cases.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

class Solution:

    def reverse_vowels(self, s: str) -> str:
        vowels = tuple('aeiouAEIOU')
        stack = []
        for char in s[::-1]:
            if char in vowels:
                stack.append(char)
        s_vector = list(s)
        for i in range(len(s_vector)):
            if s_vector[i] in vowels:
                s_vector[i] = stack.pop(0)
        return ''.join(s_vector)

