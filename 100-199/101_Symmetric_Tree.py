# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#
# Example 1:
#     1
#    / \
#   2   2
#  /|  /|
# 3 4 4 3
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
# Example 2:
#   1
#  / \
# 2   2
#  \   \
#   3   3
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
# Follow up: Could you solve it both recursively and iteratively?


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     # recursive
    #     # time complexity O(n)
    #     # space complexity O(n)
    #     def ismirrow(root1: TreeNode, root2: TreeNode) -> bool:
    #         if root1 and root2:
    #             return (
    #                 root1.val == root2.val
    #                 and ismirrow(root1.left, root2.right)
    #                 and ismirrow(root1.right, root2.left)
    #             )
    #         elif root1 or root2:
    #             return False
    #         else:
    #             return True
    #
    #     return ismirrow(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        # iterative
        # time complexity O(n)
        # space complexity O(n)
        l, r = deque([root.left]), deque([root.right])

        while l and r:
            lnode = l.pop()
            rnode = r.pop()
            if lnode and rnode:
                if lnode.val != rnode.val:
                    return False
                l.extendleft([lnode.left, lnode.right])
                r.extendleft([rnode.right, rnode.left])
            elif lnode or rnode:
                return False

        return len(l) == len(r)
