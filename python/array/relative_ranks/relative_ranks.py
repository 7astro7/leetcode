
"""
You are given an integer array score of size n, where score[i] is the
score of the ith athlete in a competition. All the scores are 
guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place 
athlete has the highest score, the 2nd place athlete has the 2nd 
highest score, and so on. The placement of each athlete determines 
their rank:
    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:
    n == score.length
    1 <= n <= 1e4
    0 <= score[i] <= 1e6
    All the values in score are unique.
"""

from queue import SimpleQueue

class Solution:

    def find_relative_ranks(self, score: list) -> list:
        Q = SimpleQueue()
        score_tuple = tuple(sorted(score, reverse = True))
        for i in range(len(score_tuple)):
            Q.put((i + 1, score_tuple[i])) 
        answer = dict()
        while not Q.empty():
            rank, val = Q.get()
            if rank < 4:
                if rank == 1:
                    answer[val] = "Gold Medal"
                if rank == 2:
                    answer[val] = "Silver Medal"
                if rank == 3:
                    answer[val] = "Bronze Medal"
            else:
                answer[val] = str(rank)
        answerboi = []
        for i in score:
            answerboi.append(answer[i])
        return answerboi

