# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.
#
# Example 1:
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
#
# Example 2:
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4


from collections import Counter
from typing import List


class Solution:
    # def deleteAndEarn(self, nums: List[int]) -> int:
    #     # Time Complexity O(n log n)
    #     # Space Complexity O(1)
    #     c = Counter(nums)
    #     pn = None
    #     pe, pd = 0, 0

    #     for n in sorted(c):
    #         if pn == n - 1:
    #             pe, pd = pd + n * c[n], max(pe, pd)
    #         else:
    #             pe, pd = max(pe, pd) + n * c[n], max(pe, pd)
    #         pn = n

    #     return max(pe, pd)

    def deleteAndEarn(self, nums: List[int]) -> int:
        # Time Complexity O(n log n)
        # Space Complexity O(n)
        def dp(i):
            n = s_nums[i]
            if i == 0:
                mem[i] = n * c[n], 0
            if i not in mem:
                if s_nums[i - 1] == n - 1:
                    mem[i] = n * c[n] + dp(i - 1)[1], max(dp(i - 1))
                else:
                    mem[i] = n * c[n] + max(dp(i - 1)), max(dp(i - 1))

            return mem[i]

        c = Counter(nums)
        s_nums = sorted(c.keys())

        mem = {}

        return max(dp(len(s_nums) - 1))
