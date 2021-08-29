# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
# of the non-overlapping intervals that cover all the intervals in the input.
# 
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# 
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time complexity: O(n log(n))
        # space complexity: O(log(n)) for sort inplace
        intervals.sort()
        
        ans = [intervals[0].copy()]
        
        for s, e in intervals:
            if s <= ans[-1][1]:
                if e > ans[-1][1]:
                    ans[-1][1] = e
            else:
                ans.append([s, e])
        
        return ans