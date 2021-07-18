# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two
# different nodes in the tree.
#
# Example 1:
#     1
#    / \
#   2   6
#  / \
# 1   3
# Input: root = [4,2,6,1,3]
# Output: 1
#
# Example 2:
#   1
#  / \
# 0   48
#    / \
#   12  49
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
# Constraints:
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5
#
# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inord(node):
            if node:
                yield from inord(node.left)
                yield node.val
                yield from inord(node.right)

        a, b = None, -(10 ** 5)
        m = 10 ** 5

        for v in inord(root):
            a, b = b, v
            m = min(m, b - a)

        return m
