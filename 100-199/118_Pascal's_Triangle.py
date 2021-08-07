# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
# 1 <= numRows <= 30


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans: List[List[int]] = []

        for i in range(1, numRows + 1):
            new_row = [1] * i

            for j in range(i - 2):
                new_row[j + 1] = ans[-1][j] + ans[-1][j + 1]

            ans.append(new_row)

        return ans
