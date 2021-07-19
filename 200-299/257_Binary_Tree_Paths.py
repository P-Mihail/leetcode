# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
# Example 1:
#   1
#  / \
# 2   3
#  \
#   5
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#
# Example 2:
# Input: root = [1]
# Output: ["1"]
#
# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100


from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #     ans = []
    #
    #     stack: List[Tuple[TreeNode, str]] = [(root, str(root.val))]
    #
    #     while stack:
    #         node, path = stack.pop()
    #
    #         if node.left is None and node.right is None:
    #             ans.append(path)
    #
    #         if node.left:
    #             stack.append((node.left, f"{path}->{node.left.val}"))
    #         if node.right:
    #             stack.append((node.right, f"{path}->{node.right.val}"))
    #
    #     return ans

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        stack: List[Tuple[TreeNode, List[str]]] = [(root, [])]

        while stack:
            node, path = stack.pop()

            if node.left is None and node.right is None:
                ans.append("->".join(path + [str(node.val)]))

            if node.left:
                stack.append((node.left, path + [str(node.val)]))
            if node.right:
                stack.append((node.right, path + [str(node.val)]))

        return ans
