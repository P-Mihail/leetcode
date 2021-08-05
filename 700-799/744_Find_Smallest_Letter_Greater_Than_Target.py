# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest
# character in the array that is larger than target.
#
# Note that the letters wrap around.
#
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
#
#
# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#
# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#
# Example 3:
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#
# Example 4:
# Input: letters = ["c","f","j"], target = "g"
# Output: "j"
#
# Example 5:
# Input: letters = ["c","f","j"], target = "j"
# Output: "c"
#
#
# Constraints:
# 2 <= letters.length <= 10^4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.


from typing import List
import bisect


class Solution:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     # time complexity O(log n)
    #     # space complexity O(1)
    #     return letters[bisect.bisect(letters, target) % len(letters)]

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # time complexity O(log n)
        # space complexity O(1)
        pl, pr = 0, len(letters) - 1

        while pl <= pr:
            m = (pl + pr) // 2

            if letters[m] <= target:
                pl = m + 1
            else:
                pr = m - 1

        return letters[pl % len(letters)]
