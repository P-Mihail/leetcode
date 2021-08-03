# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


from typing import List


class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     # time complexity O(n * 2^n)
    #     # space complexity O(n * 2^ n)
    #     nums.sort()
    #     ans: List[List[int]] = [[]]
    #     hs = set(tuple([]))
    #     for n in nums:
    #         tmp = [x.copy() for x in ans]
    #         for t in tmp:
    #             newsubset = t + [n]
    #             tnewsubset = tuple(newsubset)
    #             if tnewsubset not in hs:
    #                 ans.append(newsubset)
    #                 hs.add(tnewsubset)
    #     return ans

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # time complexity O(n * 2^n)
        # space complexity O(n * 2^ n)
        nums.sort()
        ans: List[List[int]] = [[]]
        cur: List[List[int]] = [[]]

        for i, n in enumerate(nums):
            if i == 0 or nums[i - 1] != n:
                cur = [c + [n] for c in ans]
            else:
                cur = [c + [n] for c in cur]
            ans += cur

        return ans
