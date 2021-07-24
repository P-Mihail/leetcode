# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value
# sequence.
#     3
#    / \
#   5   1
#  /|   |\
# 6 2   9 8
#  / \
# 7   4
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
# Example 1:
#     3         3
#    / \       / \
#   5   1     5   1
#  /|   |\   /|   |\
# 6 2   9 8 6 7   4 2
#  / \             / \
# 7   4           9   8
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
# Example 2:
# Input: root1 = [1], root2 = [1]
# Output: true
#
# Example 3:
# Input: root1 = [1], root2 = [2]
# Output: false
#
# Example 4:
# Input: root1 = [1,2], root2 = [2,2]
# Output: true
#
# Example 5:
#   1          1
#  / \   ->   / \
# 2   3      3   2
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].


from typing import List, Iterable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    #     def dfs(node: TreeNode) -> Iterable[int]:
    #         if node is not None:
    #             if node.left is None and node.right is None:
    #                 yield node.val
    #             yield from dfs(node.left)
    #             yield from dfs(node.right)
    #
    #     return list(dfs(root1)) == list(dfs(root2))

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root: TreeNode) -> List[int]:
            stack = [root]
            ans = []

            while stack:
                node = stack.pop()
                if node:
                    if node.left is None and node.right is None:
                        ans.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
            return ans

        return helper(root1) == helper(root2)
