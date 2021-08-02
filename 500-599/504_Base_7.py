# Given an integer num, return a string of its base 7 representation.
#
#
#
# Example 1:
# Input: num = 100
# Output: "202"
#
# Example 2:
# Input: num = -7
# Output: "-10"
#
#
# Constraints:
#
# -10^7 <= num <= 10^7


from collections import deque
from typing import Deque


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        ans: Deque[str] = deque()
        n = abs(num)

        while n > 0:
            n, r = divmod(n, 7)
            ans.appendleft(str(r))

        return ("-" if num < 0 else "") + "".join(ans)
