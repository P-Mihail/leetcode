# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
# 1
#  \
#   2
#  /
# 3
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Example 2:
# Input: root = []
# Output: []
#
# Example 3:
# Input: root = [1]
# Output: [1]
#
# Example 4:
#   1
#  /
# 2
# Input: root = [1,2]
# Output: [2,1]
#
# Example 5:
# 1
#  \
#   2
# Input: root = [1,null,2]
# Output: [1,2]
#
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     def iter(node):
    #         if node:
    #             yield from iter(node.left)
    #             yield node.val
    #             yield from iter(node.right)
    #
    #     return [x for x in iter(root)]

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        ans, stack = [], [(root, False)]

        while stack:
            node, vizited = stack.pop()
            if not node:
                continue
            elif vizited:
                ans.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

        return ans
