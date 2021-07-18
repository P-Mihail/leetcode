# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
# multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
#
# Example 1:
# 1->2->3->4->5
# 2->1->4->3->5
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
# Example 2:
# 1->2->3->4->5
# 3->2->1->4->5
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
# Example 3:
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
#
# Example 4:
# Input: head = [1], k = 1
# Output: [1]
#
#
# Constraints:
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
#
# Follow-up: Can you solve the problem in O(1) extra memory space?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        if head == None:
            return None

        dummy = tail = ListNode()
        dummy.next = head

        while head:
            start = head
            count = 0
            while count < k and head:
                head = head.next
                count += 1
            if count == k:
                prv = None
                new_tail = start
                while count > 0:
                    nxt = start.next
                    start.next = prv
                    prv = start
                    start = nxt
                    count -= 1
                tail.next = prv
                tail = new_tail
            else:
                tail.next = start

        return dummy.next
