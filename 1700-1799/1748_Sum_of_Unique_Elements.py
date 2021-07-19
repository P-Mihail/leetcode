# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the
# array.
#
# Return the sum of all the unique elements of nums.
#
#
# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
#
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
#
# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
#
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


from typing import List

# from collections import Counter


class Solution:
    # def sumOfUnique(self, nums: List[int]) -> int:
    #     counter = Counter(nums)
    #     return sum(c for c in counter if counter[c] == 1)

    # def sumOfUnique(self, nums: List[int]) -> int:
    #     hs = {}
    #     ans = 0
    #     for n in nums:
    #         hs[n] = hs.get(n, 0) + 1
    #         if hs[n] == 1:
    #             ans += n
    #         elif hs[n] == 2:
    #             ans -= n
    #
    #     return ans

    def sumOfUnique(self, nums: List[int]) -> int:
        s1 = set()
        s2 = set()
        ans = 0

        for n in nums:
            if n in s1:
                if not n in s2:
                    s2.add(n)
                    ans -= n
            else:
                s1.add(n)
                ans += n

        return ans
