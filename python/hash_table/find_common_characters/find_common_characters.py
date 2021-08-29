
"""
Given a string array words, return an array of all characters that 
show up in all strings within the words (including duplicates). You 
may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.

"""

class Solution:

    def common_chars(self, words: list) -> list:
        common = set(words[0])
        for word in words:
            common.intersection_update(word)
        common = list(common)
        counts = {c: words[0].count(c) for c in words[0] if c in common}
        for word in words[1:]:
            count = {k: word.count(k) for k in word if k in common}
            for k in count:
                if count[k] < counts[k]:
                    counts[k] = count[k] 
        answer = []
        for k in counts.keys():
            temp = [k,] * counts[k] 
            answer.extend(temp) 
        return answer

