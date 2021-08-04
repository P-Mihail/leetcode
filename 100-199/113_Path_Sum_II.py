# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals
# targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#      [5]
#      / \
#    [4] [8]
#    /   / \
#  [11] 13 [4]
#  / \     / \
# 7  [2] [5]  1
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
# Example 2:
#   1
#  / \
# 2   3
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    #     # recursive
    #     if root is None:
    #         return []
    #
    #     if root.left is None and root.right is None and root.val == targetSum:
    #         return [[root.val]]
    #
    #     return [
    #         [root.val] + path
    #         for path in self.pathSum(root.left, targetSum - root.val)
    #         + self.pathSum(root.right, targetSum - root.val)
    #         if path
    #     ]

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # iterative
        ans = []

        if root:
            stack: List[Tuple[TreeNode, List[int], int]] = [(root, [], targetSum)]

            while stack:
                node, path, target = stack.pop()

                if node:
                    if node.left or node.right:
                        stack.append((node.left, path + [node.val], target - node.val))
                        stack.append((node.right, path + [node.val], target - node.val))
                    else:
                        if target == node.val:
                            ans.append(path + [node.val])

        return ans
