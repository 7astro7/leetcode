
# We have a collection of stones, each stone has a positive integer 
# weight. Each turn, we choose the two heaviest stones and smash them
# together. Suppose the stones have weights x and y with x <= y.  The
# result of this smash is:
#   If x == y, both stones are totally destroyed;
#   If x != y, the stone of weight x is totally destroyed, and the 
#   stone of weight y has new weight y-x.

# At the end, there is at most 1 stone left. Return the weight of 
# this stone (or 0 if there are no stones left.)

# Example 1:
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
#   We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
#   we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
#   we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
#   we combine 1 and 1 to get 0 so the array converts to [1] then 
#   that's the value of last stone.

# Note:
#    1 <= stones.length <= 30
#    1 <= stones[i] <= 1000

import heapq

class Solution:

    def _check_preconditions(self, stones):
        if not 1 <= len(stones) <= 30:
            raise Exception("Invalid len(stones)")
        if min(stones) < 1 or max(stones) > 1e3:
            raise ValueError("!(1 <= stones[i] <= 1e3)")

    def last_stone_weight(self, stones: list) -> int:
        if len(stones) == 1:    # trivial case 
            return stones[0]
        self._check_preconditions(stones)
        stone_heap = []
        for a_stone in stones:
            a_stone **= -1
            heapq.heappush(stone_heap, a_stone)
        while len(stone_heap) > 1:
            stone_y = heapq.heappop(stone_heap) ** -1
            stone_x = heapq.heappop(stone_heap) ** -1
            new_stone_weight = stone_y - stone_x
            if new_stone_weight != 0:
                heapq.heappush(stone_heap, new_stone_weight ** -1)
        if len(stone_heap) == 0:
            return 0
        return round(stone_heap[0] ** -1)

if __name__ == "__main__":
    Solution()
