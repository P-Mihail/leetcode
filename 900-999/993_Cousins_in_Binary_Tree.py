# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
#
# Example 1:
#     1
#    / \
#   2   3
#  /
# 4
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Example 2:
#     1
#    / \
#   2   3
#    \   \
#     4   5
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
# Example 3:
#     1
#    / \
#   2   3
#    \
#     4
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#
#
# Constraints:
# The number of nodes in the tree will be between 2 and 100.


from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack: List[Tuple[TreeNode, int, Optional[TreeNode]]] = [(root, 0, None)]

        while stack:
            node, depth, parent = stack.pop()
            if node.val == x:
                x_depth = depth
                x_parent = parent
            if node.val == y:
                y_depth = depth
                y_parent = parent
            if node.left:
                stack.append((node.left, depth + 1, node))
            if node.right:
                stack.append((node.right, depth + 1, node))

        return x_depth == y_depth and x_parent != y_parent
