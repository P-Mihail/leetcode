# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
#
# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Example 4:
# Input: x = -101
# Output: false
#
# Constraints:
#
# -2^31 <= x <= 2^31 - 1
#
#
# Follow up: Could you solve it without converting the integer to a string?


class Solution(object):
    # def isPalindrome(self, x: int) -> bool:
    #     # unfair solution due to using conversion to string
    #     x = str(x)
    #     if x == x[::-1]:
    #         return True
    #     else:
    #         return False

    def isPalindrome(self, x: int) -> bool:
        # time complexity: O(log10 n)
        # space complexity: O(1)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        tmp = 0
        while tmp < x:
            tmp, x = tmp * 10 + x % 10, x // 10

        return tmp == x or tmp // 10 == x
