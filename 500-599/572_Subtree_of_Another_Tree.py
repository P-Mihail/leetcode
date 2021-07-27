# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree
# tree could also be considered as a subtree of itself.
#
#
# Example 1:
#     3
#    / \
#   4   5     4
#  / \       / \
# 1   2     1   2
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
#     3
#    / \
#   4   5     4
#  / \       / \
# 1   2     1   2
#    /
#   0
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSame(root1: TreeNode, root2: TreeNode) -> bool:
            if root1 and root2:
                return (
                    root1.val == root2.val
                    and isSame(root1.left, root2.left)
                    and isSame(root1.right, root2.right)
                )
            elif root1 or root2:
                return False
            else:
                return True

        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if isSame(node, subRoot):
                    return True
                stack.extend([node.left, node.right])

        return False
