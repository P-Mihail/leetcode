# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  / \       \
# 7  2        1
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#
# Example 2:
#   1
#  / \
# 2   3
# Input: root = [1,2,3], targetSum = 5
# Output: false
#
# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: false
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    #     if not root:
    #         return False
    #
    #     if not root.left and not root.right:
    #         return targetSum == root.val
    #
    #     return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, cursum = stack.pop()

            if not node.left and not node.right:
                if cursum == targetSum:
                    return True
                else:
                    continue

            for child in [node.left, node.right]:
                if child:
                    stack.append((child, cursum + child.val))

        return False
