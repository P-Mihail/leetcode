# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes 
# with a value greater than X.
# Return the number of good nodes in the binary tree.
# 
# Example 1:
#      [3]
#      / \
#     1  [4]
#    /   / \
#  [3]   1  [5]
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# 
# Example 2:
#     [3]
#     /
#   [3]
#   / \
# [4]  2
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# 
# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
# 
# Constraints:
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def goodNodes(self, root: TreeNode) -> int:
    #     # recursive
    #     def dfs(node, val):
    #         if node is None:
    #             return 0
            
    #         ans = 0
    #         if node.val >= val:
    #             ans += 1
    #             val = node.val
            
    #         return ans + dfs(node.left, val) + dfs(node.right, val)
        
    #     return dfs(root, root.val)

    def goodNodes(self, root: TreeNode) -> int:
        # iterative
        ans = 0
        stack = [(root, root.val)]
        
        while stack:
            node, v = stack.pop()
            if node is not None:
                if node.val >= v:
                    ans += 1
                    v = node.val
                stack.extend([(node.left, v), (node.right, v)])
        
        return ans
