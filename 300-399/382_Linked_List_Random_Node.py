# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
#
# Implement the Solution class:
#   Solution(ListNode head) Initializes the object with the integer array nums.
#   int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.
#
# Example 1:
# (1) -> (2) -> (3)
# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
#
# Constraints:
# The number of nodes in the linked list will be in the range [1, 104].
# -10^4 <= Node.val <= 10^4
# At most 10^4 calls will be made to getRandom.
#
# Follow up:
#   What if the linked list is extremely large and its length is unknown to you?
#   Could you solve this efficiently without using extra space?


import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n = 1
        cur = 0
        point = self.head
        while point:
            if random.random() < 1 / n:
                cur = point.val
            point = point.next
            n += 1
        return cur


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
