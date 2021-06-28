# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
# connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
#
# Example 1:
# 3 -> 2 -> 0 -> -4
#      ^          |
#      ------------
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
# 1 -> 2
# ^    |
# ------
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
# Example 3:
# 1
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution(object):
    # def hasCycle(self, head: ListNode) -> bool:
    #     # time complexity O(n)
    #     # space complexity O(n)
    #     hashset = set()
    #
    #     while head:
    #         if head in hashset:
    #             return True
    #         hashset.add(head)
    #         head = head.next
    #
    #     return False
    #
    # def hasCycle(self, head: ListNode) -> bool:
    #     # 2 pointers
    #     # time complexity O(n)
    #     # space complexity O(1)
    #     if head is None:
    #         return False
    #
    #     p1, p2 = head, head.next
    #
    #     while p1 != p2:
    #         if p1.next and p2.next and p2.next.next:
    #             p1 = p1.next
    #             p2 = p2.next.next
    #         else:
    #             return False
    #
    #     return True

    def hasCycle(self, head: ListNode) -> bool:
        # 2 pointers
        # time complexity O(n)
        # space complexity O(1)
        p1, p2 = head, head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True

        return False
