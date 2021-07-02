# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary
# search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by
# more than one.
#
#
# Example 1:
#      0
#     / \
#   -3   9
#   /   /
# -10  5
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#      0
#     / \
#   -10  5
#     \   \
#     -3   9
#
# Example 2:
#    3       1
#   /         \
#  1           3
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
#
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #     if len(nums) == 0:
    #         return None
    #
    #     idx = len(nums) // 2
    #
    #     return TreeNode(
    #         nums[idx],
    #         self.sortedArrayToBST(nums[:idx]),
    #         self.sortedArrayToBST(nums[idx + 1 :]),
    #     )

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def node(s: int, e: int) -> Optional[TreeNode]:
            if s == e:
                return None
            else:
                idx = (s + e) // 2
                return TreeNode(nums[idx], node(s, idx), node(idx + 1, e))

        return node(0, len(nums))