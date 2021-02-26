
# Given an integer numRows, return the first numRows of Pascal's 
# triangle.

# In Pascal's triangle, each number is the sum of the two numbers 
# directly above it as shown:

#             1
#           1   1
#         1   2   1 
#       1   3   3   1
#     1   4   6   4   1

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

# Constraints:
#    1 <= numRows <= 30

class Solution:

    def __init__(self):
        self.__matrix = []

    def _next_row(self, prev_row: list) -> list:
        padded_row = [0,] + prev_row + [0,]
        next_row = []
        i = 0
        while len(next_row) < len(padded_row) - 1:
            next_row.append(padded_row[i] + padded_row[i + 1])
            i += 1
        return next_row

    def generate(self, num_rows: int) -> list:
        next_row = [1,]
        self.__matrix.append(next_row)
        while True:
            if len(self.__matrix) == num_rows:
                return self.__matrix
            next_row = self._next_row(next_row)
            self.__matrix.append(next_row)


if __name__ == "__main__":
    Solution()

