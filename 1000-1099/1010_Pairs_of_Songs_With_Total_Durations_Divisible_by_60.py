# You are given a list of songs where the ith song has a duration of time[i] seconds.
#
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want
# the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
#
# Example 1:
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
#
# Example 2:
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
#
# Constraints:
# 1 <= time.length <= 6 * 10^4
# 1 <= time[i] <= 500


from typing import Dict, List

# from collections import defaultdict


class Solution(object):
    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     # time complexity O(n), 1 pass
    #     # space comlexity O(1)
    #     ht: Dict[int, int] = defaultdict(int)
    #     count = 0
    #     for song in time:
    #         count += ht[-song % 60]
    #         ht[song % 60] += 1
    #     return count

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # time complexity O(n), 1 pass
        # space comlexity O(1)
        cache = [0] * 60
        ans = 0

        for t in time:
            ans += cache[-t % 60]
            cache[t % 60] += 1

        return ans

