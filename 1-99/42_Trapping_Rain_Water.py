# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it can trap after raining.
#
#
# Example 1:
# |       X
# |   X***XX*X
# | X*XX*XXXXXX
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
# 6 units of rain water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5


class Solution:
    def trap(self, height):
        # time complexity O(n)
        # space complexity O(n)
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h)
            waterLevel += [left]

        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h
        return sum(waterLevel)
