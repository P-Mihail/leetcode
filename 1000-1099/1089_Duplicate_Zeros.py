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


from typing import List

# from typing import Deque
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

    # def duplicateZeros(self, arr: List[int]) -> None:
    #     # inplace modifications
    #     i = 0
    #     while i < len(arr):
    #         if arr[i] == 0:
    #             arr.insert(i, 0)
    #             arr.pop()
    #             i += 2
    #         else:
    #             i += 1

    def duplicateZeros(self, arr: List[int]) -> None:
        # time complexity: O(n)
        # space complexity: O(1)
        count_zeros = 0
        is_edge_case = False  # The sequence will end with one zero

        for i, num in enumerate(arr):
            if i + count_zeros >= len(arr):
                break

            if num == 0:
                if i + count_zeros == len(arr) - 1:
                    is_edge_case = True
                count_zeros += 1

        from_pointer = len(arr) - 1 - count_zeros
        to_pointer = len(arr) - 1
        if is_edge_case:
            arr[-1] = 0
            to_pointer -= 1

        while from_pointer < to_pointer:
            if arr[from_pointer] == 0:
                arr[to_pointer] = 0
                to_pointer -= 1
            arr[to_pointer] = arr[from_pointer]
            to_pointer -= 1
            from_pointer -= 1
