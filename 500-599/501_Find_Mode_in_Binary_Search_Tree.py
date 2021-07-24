# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently
# occurred element) in it.
#
# If the tree has more than one mode, return them in any order.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
# 1
#  \
#   2
#  /
# 2
# Input: root = [1,null,2,2]
# Output: [2]
#
# Example 2:
# Input: root = [0]
# Output: [0]
#
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
#
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to
# recursion does not count).


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        count = 0
        prevV = root.val + 1
        prevC = 0

        def search(node: TreeNode) -> None:
            nonlocal ans, count, prevV, prevC

            if node is None:
                return

            search(node.left)

            if node.val == prevV:
                prevC += 1
            else:
                prevV = node.val
                prevC = 1

            if prevC == count:
                ans.append(node.val)
            elif prevC >= count:
                count = prevC
                ans = [node.val]

            search(node.right)

        search(root)

        return ans
