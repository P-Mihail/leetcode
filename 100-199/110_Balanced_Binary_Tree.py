# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# 
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#   3
#  / \
# 9   20
#    / \
#   15  7
# Example 2:
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# Example 3:
# Input: root = []
# Output: true
# 
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4



from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> Tuple[int, bool]:
            if root is None:
                return 0, True
            
            hl, isbl = helper(root.left)
            hr, isbr = helper(root.right)
            
            return max(hl, hr) + 1, isbl and isbr and abs(hl - hr) <= 1
        
        return helper(root)[1]
