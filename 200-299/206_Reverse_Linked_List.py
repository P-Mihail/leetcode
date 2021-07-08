# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []
#
# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     # iterative
    #     # time complexity O(n)
    #     # space complexity O(1)
    #     prev_node = None
    #     cur_node = head
    #     while cur_node:
    #         cur_node.next, cur_node, prev_node = prev_node, cur_node.next, cur_node
    #     return prev_node

    def reverseList(self, head: ListNode) -> ListNode:
        # recursive
        # time complexity O(n)
        # space complexity O(n)
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return node
