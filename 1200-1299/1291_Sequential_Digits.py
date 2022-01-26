# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
#
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
#
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
#
# Constraints:
# 10 <= low <= high <= 10^9


from typing import List
from math import floor, log10


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = list()

        for window in range(floor(log10(low)) + 1, floor(log10(high)) + 2):
            for start in range(10 - window):
                number = 0
                for i in range(start, start + window):
                    number = number * 10 + i + 1

                if low <= number <= high:
                    res.append(number)

        return res
