# You are given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some 
# continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.
# Return the maximum points you can get.
# 
# Example 1:
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# 
# Example 2:
# Input: boxes = [1,1,1]
# Output: 9
# 
# Example 3:
# Input: boxes = [1]
# Output: 1
# 
# Constraints:
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100


from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(maxsize=None)
        def fn(lo, hi, k):
            if lo == hi:
                return 0
            while lo + 1 < hi and boxes[lo] == boxes[lo + 1]:
                lo += 1
                k += 1
            ans = (k + 1) ** 2 + fn(lo + 1, hi, 0)

            for p in range(lo + 2, hi):
                if boxes[p] == boxes[lo]:
                    ans = max(ans, fn(lo + 1, p, 0) + fn(p, hi, k + 1))

            return ans

        return fn(0, len(boxes), 0)
