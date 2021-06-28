# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Example 1:
#     1
#      \
#       2
#      /
#     3
# Input: root = [1,null,2,3]
# Output: [1,2,3]
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
#     1
#    /
#   2
# Input: root = [1,2]
# Output: [1,2]
#
# Example 5:
#     1
#      \
#       2
# Input: root = [1,null,2]
# Output: [1,2]
#
#
# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
# Follow up: Recursive solution is trivial, could you do it iteratively?


from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution(object):
#     # use generator
#     def gen(self, node):
#         if node:
#             yield node.val
#             yield from self.gen(node.left)
#             yield from self.gen(node.right)
#
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         return list(self.gen(root))


class Solution(object):
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        stack, ans = [root], []

        while len(stack) > 0:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return ans
