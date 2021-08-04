# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along
# the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from
# parent nodes to child nodes).
#
#
# Example 1:
#        10
#        / \
#       5  -3
#      / \   \
#     3   2   11
#    / \   \
#   3  -2   1
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are [5, 3], [5, 2, 1] and [-3, 11].
#
# Example 2:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000


from typing import Dict, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #     ans = 0
    #
    #     if root:
    #         stack: List[Tuple[TreeNode, List[int]]] = [(root, [])]
    #
    #         while stack:
    #             node, sums = stack.pop()
    #             if node:
    #                 newsums = [node.val] + [s + node.val for s in sums]
    #                 ans += newsums.count(targetSum)
    #                 stack.append((node.left, newsums))
    #                 stack.append((node.right, newsums))
    #
    #     return ans

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # more efficient
        ans = 0

        if root:
            stack: List[Tuple[TreeNode, Dict[int, int]]] = [(root, {})]

            while stack:
                node, sums = stack.pop()

                newsums = {k + node.val: v for k, v in sums.items()}
                newsums[node.val] = newsums.get(node.val, 0) + 1
                ans += newsums.get(targetSum, 0)
                if node.left:
                    stack.append((node.left, newsums))
                if node.right:
                    stack.append((node.right, newsums))

        return ans
