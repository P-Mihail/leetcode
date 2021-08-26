# One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record 
# the node's value. If it is a null node, we record using a sentinel value such as '#'.
#      9
#     / \
#    3   2
#   / \   \
#  4   1   6
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' 
# represents a null node.
# Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization 
# of a binary tree.
# It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' 
# representing null pointer.
# You may assume that the input format is always valid.
# For example, it could never contain two consecutive commas, such as "1,,3".
# Note: You are not allowed to reconstruct the tree.
# 
# Example 1:
# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# Input: preorder = "1,#"
# Output: false
# 
# Example 3:
# Input: preorder = "9,#,#,1"
# Output: false
# 
# Constraints:
# 1 <= preorder.length <= 10^4
# preoder consist of integers in the range [0, 100] and '#' separated by commas ','.


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        l = preorder.split(",")
        if len(l) >= 3 and (preorder[0] == '#' or len(l) % 2 == 0 or l[-1] != "#" or l[-2] != "#"):
            return False

        stack = l[:2]
        for n in l[2:]:
            stack.append(n)
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                if stack[-1] == '#':
                    return False
                stack[-1] = '#'

        return len(stack) == 1 and stack[-1] == '#'
