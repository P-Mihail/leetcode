# Given the head of a singly linked list, return true if it is a palindrome.
# 
# Example 1:
# 1 -> 2 -> 2 -> 1
# Input: head = [1,2,2,1]
# Output: true
# 
# Example 2:
# 1 -> 2
# Input: head = [1,2]
# Output: false
# 
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
# 
# Follow up: Could you do it in O(n) time and O(1) space?

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # time complexity O(n)
        # space complexity O(1)
        pf = pl = head
        prev = None
        while pf is not None and pf.next is not None:
            pf = pf.next.next
            pl.next, pl, prev = prev, pl.next, pl
        
        if pf is not None: #нечет число нод
            pl = pl.next
        
        while pl:
            if pl.val != prev.val:
                return False
            pl, prev = pl.next, prev.next
        
        return True
