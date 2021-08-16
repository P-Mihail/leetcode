# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the
# others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node
# of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
#
# Example 1:
#     1         2              3
#    / \       / \            / \
#   3   2  +  1   3    ->    4   5
#  /           \   \        / \   \
# 5             4   7      5   4   7
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#
# Constraints:
# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # recursion
    #     # time complexity O(m), m - total of nodes to be traversed (minimum number of nodes from the two given trees).
    #     # space complexity O(m), m -  The depth of the recursion tree can go upto m in the case of a skewed tree.
    #     # In average case, depth will be O(logm).
    #     if root1 is None:
    #         return root2

    #     if not root2 is None:
    #         root1.val += root2.val
    #         root1.left = self.mergeTrees(root1.left, root2.left)
    #         root1.right = self.mergeTrees(root1.right, root2.right)

    #     return root1

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative
        # time complexity O(m), m - total of nodes to be traversed (minimum number of nodes from the two given trees).
        # space complexity O(m), m - the depth of stack can grow upto m in case of a skewed tree.
        # In average case, depth will be O(logm)
        if root1 is None:
            return root2

        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()

            if node2 is not None:
                node1.val += node2.val
                if node1.left is None:
                    node1.left = node2.left
                else:
                    stack.append((node1.left, node2.left))
                if node1.right is None:
                    node1.right = node2.right
                else:
                    stack.append((node1.right, node2.right))

        return root1
