# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
# Example 1:
# 1
#  \
#   2
#  /
# 3
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# Output: [2,1]
#
#
# Constraints:
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     # recursive
    #     if root:
    #         return [
    #             *self.postorderTraversal(root.left),
    #             *self.postorderTraversal(root.right),
    #             root.val,
    #         ]
    #     else:
    #         return []

    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     # by generator
    #     def postordergen(node):
    #         if node:
    #             yield from postordergen(node.left)
    #             yield from postordergen(node.right)
    #             yield node.val
    #
    #     return list(postordergen(root))

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        stack = [(root, False)]
        ans = []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return ans
