# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product
# of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large,
# return it modulo 10^9 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.
#
# Example 1:
#      1        1
#     / \        \
#    2   3    2   3
#   /|  /    /|  /
#  4 5 6    4 5 6
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
#
# Example 2:
# 1       1
#  \       \
#   2       2
#  / \     /
# 3   4   3   4
#    / \     / \
#   5   6   5   6
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
#
# Example 3:
# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
#
# Example 4:
# Input: root = [1,1]
# Output: 1
#
# Constraints:
# The number of nodes in the tree is in the range [2, 5 * 10^4].
# 1 <= Node.val <= 10^4


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def maxProduct(self, root: Optional[TreeNode]) -> int:
    #     # recursive
    #     sums = []

    #     def dfs(node):
    #         if node is None:
    #             return 0
    #         subtree_sum = dfs(node.left) + dfs(node.right) + node.val
    #         sums.append(subtree_sum)
    #         return subtree_sum

    #     m = -inf
    #     total = dfs(root)
    #     for i in sums:
    #         prod = i * (total-i)
    #         if prod > m:
    #             m = prod

    #     return m % (10**9 + 7)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # iterative
        sums = []

        stack = [(root, False)]
        hm = {}

        while stack:
            node, vizited = stack.pop()
            if vizited:
                s = node.val + hm.pop(node.left, 0) + hm.pop(node.right, 0)
                hm[node] = s
                sums.append(s)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))

        total = sums[-1]

        return max((total-x)*x for x in sums) % 1_000_000_007
