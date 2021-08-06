# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
# leaf node.
#
#
#
# Example 1:
#    3
#   / \
#  9   20
#      / \
#     15  7
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
# Input: root = [1,null,2]
# Output: 2
#
# Example 3:
# Input: root = []
# Output: 0
#
# Example 4:
# Input: root = [0]
# Output: 1
#
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0

        if root:
            stack = [root]

            while stack:
                stack = [n for node in stack for n in [node.left, node.right] if n]
                ans += 1

        return ans
