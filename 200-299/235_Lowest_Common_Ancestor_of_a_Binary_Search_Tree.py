# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
# the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Example 1:
#     6
#    / \
#   2   8
#  /|   |\
# 0 4   7 9
#   |\
#   3 5
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
# Example 2:
#     6
#    / \
#   2   8
#  /|   |\
# 0 4   7 9
#   |\
#   3 5
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA
# definition.
#
# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # iterative
        # time complexity O(n) n is the number of nodes in the BST. In the worst case we might be visiting all the nodes
        # of the BST.
        # space complexity O(1)
        ancestor = root
        if p.val < q.val:
            a, b = p.val, q.val
        else:
            a, b = q.val, p.val

        while ancestor.val > b or ancestor.val < a:
            if b < ancestor.val:
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return ancestor
