# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.
#
# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
#
# Example 2:
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
# Constraints:
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9


from typing import List, Deque

# import collections


class Solution(object):
    # def duplicateZeros(self, arr: List[int]) -> None:
    #     # simple way
    #     tmp = "".join(str(x) for x in arr).replace("0", "00")
    #     for i in range(len(arr)):
    #         arr[i] = int(tmp[i])

    # def duplicateZeros(self, arr: List[int]) -> None:
    #     # additional deque
    #     q: Deque[int] = collections.deque()
    #
    #     i = 0
    #     while i < len(arr):
    #         q.appendleft(arr[i])
    #         if arr[i] == 0:
    #             q.appendleft(0)
    #         arr[i] = q.pop()
    #         i += 1

    def duplicateZeros(self, arr: List[int]) -> None:
        # inplace modifications
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1
