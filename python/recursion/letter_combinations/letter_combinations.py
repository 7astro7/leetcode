
"""
Given a string containing digits from 2-9 inclusive, return all 
possible letter combinations that the number could represent. Return 
the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

"""

class Solution:

    def __init__(self):
        self.__choices = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                }

    def _concat(
            self,
            u: tuple,
            v: tuple,
            ) -> map:
        for i in u:
            for j in v:
                yield i + j

    def letter_combinations(
            self,
            digits: str,
            ) -> list:
        if digits is None or not len(digits):
            return []
        combos = list(self.__choices[digits[0]])
        i = 1
        while True:
            if i >= len(digits):
                return combos
            v = list(self.__choices[digits[i]])
            combos = list(self._concat(combos, v))
            i += 1
