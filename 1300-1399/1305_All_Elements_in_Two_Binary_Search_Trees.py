# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.
#
# Example 1:
#   2     1
#  / \   / \
# 1   4 0   3
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
#
# Example 2:
# 1     8
#  \   /
#   8 1
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
#
# Constraints:
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def bst_inord(root):
            if root is None:
                return None

            stack = [(root, True)]
            while stack:
                node, flag = stack.pop()

                if node.left and flag:
                    stack.append((node, False))
                    stack.append((node.left, True))
                else:
                    if node.right:
                        stack.append((node.right, True))
                    yield node.val

        i1 = bst_inord(root1)
        i2 = bst_inord(root2)

        ans = []

        a = next(i1, None)
        b = next(i2, None)

        while not (a is None and b is None):
            if a is None or (not b is None and a > b):
                ans.append(b)
                b = next(i2, None)
            else:
                ans.append(a)
                a = next(i1, None)

        return ans
