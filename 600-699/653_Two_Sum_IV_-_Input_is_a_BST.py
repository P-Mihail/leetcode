# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such
# that their sum is equal to the given target.
#
#
# Example 1:
#      5
#     / \
#    3   6
#   / \   \
#  2   4   7
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#
# Example 2:
#      5
#     / \
#    3   6
#   / \   \
#  2   4   7
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
#
# Example 3:
# Input: root = [2,1,3], k = 4
# Output: true
#
# Example 4:
# Input: root = [2,1,3], k = 1
# Output: false
#
# Example 5:
# Input: root = [2,1,3], k = 3
# Output: true
#
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is guaranteed to be a valid binary search tree.
# -10^5 <= k <= 10^5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hs = set()

        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if k - node.val in hs:
                    return True
                hs.add(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return False
