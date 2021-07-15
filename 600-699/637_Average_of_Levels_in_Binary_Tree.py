# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers
# within 10-5 of the actual answer will be accepted.
#
# Example 1:
#    3
#   / \
#  9   20
#     / \
#    15  7
# Input: root = [3,9,20,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
# Example 2:
#     3
#    / \
#   9   20
#  / \
# 15  7
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -2^31 <= Node.val <= 2^31 - 1


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        nodes = [root]
        ans = []

        while nodes:
            tmp = []
            sumval = 0
            for n in nodes:
                sumval += n.val
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            ans.append(sumval / len(nodes))
            nodes = tmp

        return ans
