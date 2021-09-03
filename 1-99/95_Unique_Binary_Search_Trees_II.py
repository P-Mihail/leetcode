# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of
# unique values from 1 to n. Return the answer in any order.
#
# Example 1:
# 1    1       2      3   3
#  \    \     / \    /   / 
#   3    2   1   3  2   1
#  /      \        /     \
# 2        3      1       2
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
# Example 2:
# Input: n = 1
# Output: [[1]]
#
# Constraints:
# 1 <= n <= 8


from typing import List, Optional
from functools import lru_cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache
        def helper(arr):
            if len(arr) == 0:
                return [None]
            return [TreeNode(arr[i], l, r) for i in range(0, len(arr)) for l in helper(arr[:i]) for r in helper(arr[i + 1:])]

        return helper(tuple(range(1, n+1)))
