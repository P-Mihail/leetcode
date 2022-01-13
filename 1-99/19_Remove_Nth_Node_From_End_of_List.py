# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Example 1:
# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 2 -> 3 ------> 5
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
# Follow up: Could you do this in one pass?


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = ans = ListNode(next=head)
        p2 = head

        for _ in range(n - 1):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return ans.next
