
"""
Given a m x n matrix grid which is sorted in non-increasing order 
both row-wise and column-wise, return the number of negative numbers 
in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""

class Solution:

    
    def count_negatives(self, grid: list) -> int:
        if grid[len(grid) - 1][len(grid[0]) - 1] > 0:
            return 0
        count = 0
        for row in grid:
            if max(row) < 0:
            # then all elements are negative
                count += len(row)
            elif min(row) < 0:
            # then there are negatives
                for i in row:
                    if i < 0:
                        count += 1
        return count



