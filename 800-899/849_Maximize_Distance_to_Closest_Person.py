# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents
# that the ith seat is empty (0-indexed).
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to the closest person.
#
# Example 1:
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
#
# Example 2:
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
#
# Example 3:
# Input: seats = [0,1]
# Output: 1
#
# Constraints:
# 2 <= seats.length <= 2 * 10^4
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.


from typing import List
import math


class Solution:
    # def maxDistToClosest(self, seats: List[int]) -> int:
    #     # Time complexity O(N)
    #     # Space complexity O(N)
    #     N = len(seats)
    #     left, right = [N] * N, [N] * N

    #     for i in range(N):
    #         if seats[i] == 1:
    #             left[i] = 0
    #         elif i > 0:
    #             left[i] = left[i - 1] + 1

    #     for i in range(N - 1, -1, -1):
    #         if seats[i] == 1:
    #             right[i] = 0
    #         elif i < N - 1:
    #             right[i] = right[i + 1] + 1

    #     return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)

    def maxDistToClosest(self, seats: List[int]) -> int:
        # Time complexity O(N)
        # Space complexity O(1)
        res, dist = 0, seats.index(1)

        for seat in seats:
            if seat:
                res, dist = max(res, math.ceil(dist / 2)), 0
            else:
                dist += 1

        return max(res, dist)
