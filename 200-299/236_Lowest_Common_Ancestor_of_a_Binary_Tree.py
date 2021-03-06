# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
# the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
# Example 1:
#     3
#    / \
#   5   1
#  /|   |\
# 6 2   0 8
#   |\
#   7 4
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
#     3
#    / \
#   5   1
#  /|   |\
# 6 2   0 8
#   |\
#   7 4
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
# Constraints:
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.


from typing import Dict, Optional, Set


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution(object):
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # iterative
        # time complexity O(n) n is the number of nodes
        # space complexity O(n)
        stack = [root]
        parent: Dict[TreeNode, Optional[TreeNode]] = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node

        ancestors_p: Set[Optional[TreeNode]] = set()

        while p:
            ancestors_p.add(p)
            p = parent[p]

        while q not in ancestors_p:
            q = parent[q]

        return q
