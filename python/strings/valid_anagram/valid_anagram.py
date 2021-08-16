
"""
Given two strings s and t, return true if t is an anagram of s, and 
false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 1e4
    s and t consist of lowercase English letters.
"""

class Solution:

    def is_anagram(self, s: str, t: str) -> bool:
#        if len(s) != len(t):
#            return False
#        if set(s) != set(t):
#            return False
        if {c: s.count(c) for c in s} == {c: t.count(c) for c in t}:
            return True
        return False

