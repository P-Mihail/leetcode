# Given an array of integers nums.
#
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
# Return the number of good pairs.
#
# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
# Example 3:
# Input: nums = [1,2,3]
# Output: 0
#
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


from typing import Dict, List


class Solution(object):
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    #     ans = 0
    #     ht: Dict[int, int]  = {}
    #     for n in nums:
    #         if n in ht:
    #             ans += ht[n]
    #             ht[n] += 1
    #         else:
    #             ht[n] = 1
    #     return ans
    #
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    #     set_nums: Dict[int, int]  = {}
    #
    #     for n in nums:
    #         set_nums[n] = set_nums.get(n, 0) + 1
    #
    #     out = 0
    #     for k in set_nums:
    #         out += set_nums[k] * (set_nums[k] - 1)
    #
    #     return out // 2

    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        ht: Dict[int, int] = {}

        for n in nums:
            ans += ht.get(n, 0)
            ht[n] = ht.get(n, 0) + 1

        return ans
