# Given the root of a binary tree, return the sum of all left leaves.
# 
# Example 1:
#    3
#   / \
#  9  20
#     / \
#    15  7
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# 
# Example 2:
# 
# Input: root = [1]
# Output: 0
# 
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if node.left is not None and node.left.left is None and node.left.right is None:
                    ans += node.left.val
                stack.extend([node.left, node.right])
        
        return ans
