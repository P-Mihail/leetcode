# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may
# not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
#
#
# Example 1:
#      1
#     / \
#    2   3
#   / \
#  4   5
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Example 2:
# Input: root = [1,2]
# Output: 1
#
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100


from typing import Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     # recursive
#     class Height:
#         def __init__(self):
#             self.h = 0
#
#     def diameterOfBinaryTree(self, root: TreeNode, height=None) -> int:
#         if height is None:
#             height = self.Height()
#
#         if root is None:
#             height.h = 0
#             return 0
#
#         lh = self.Height()
#         rh = self.Height()
#
#         lr = self.diameterOfBinaryTree(root.left, lh)
#         rr = self.diameterOfBinaryTree(root.right, rh)
#
#         height.h = max(lh.h, rh.h) + 1
#
#         return max(lh.h + rh.h, lr, rr)


class Solution:
    # iterative
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        hm: Dict[TreeNode, int] = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    lh = 0 if node.left is None else hm.pop(node.left)
                    rh = 0 if node.right is None else hm.pop(node.right)
                    ans = max(ans, lh + rh)
                    hm[node] = max(lh, rh) + 1
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))
        return ans
