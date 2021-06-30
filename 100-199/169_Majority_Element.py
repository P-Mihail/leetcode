# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?


from typing import List

# from typing import Dict


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     # simple way
    #     # time complexity O(n)
    #     # space complexity O(n)
    #     counter: Dict[int, int] = {}
    #
    #     for num in nums:
    #         counter[num] = counter.get(num, 0) + 1
    #         if counter[num] > len(nums) // 2:
    #             return num
    #
    # def majorityElement(self, nums: List[int]) -> int:
    #     # time complexity O(n log n)
    #     # space complexity O(1)
    #     nums.sort()
    #     return nums[len(nums) // 2]

    def majorityElement(self, nums: List[int]) -> int:
        #  Boyer Moore Algorithm
        # time complexity O(n)
        # space complexity O(1)
        count = 0
        candidate = nums[0]

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
