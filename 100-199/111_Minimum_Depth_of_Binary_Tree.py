# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
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
# Output: 2
#
# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ans = 0

        if root:
            stack = [root]
            while stack:
                newstack = []
                ans += 1

                for node in stack:
                    if node:
                        if node.left is None and node.right is None:
                            return ans
                        newstack.extend([node.left, node.right])
                stack = newstack

        return ans
