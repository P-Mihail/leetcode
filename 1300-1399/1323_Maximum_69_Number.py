# Given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
#
#
# Example 1:
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
#
# Example 2:
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
#
# Example 3:
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
#
#
# Constraints:
#
# 1 <= num <= 10^4
# num's digits are 6 or 9.


class Solution:
    # def maximum69Number(self, num: int) -> int:
    #     ans = num
    #     i, mini = 0, -1
    #
    #     while num > 0:
    #         num, n = divmod(num, 10)
    #         if n == 6:
    #             mini = i
    #         i += 1
    #
    #     return ans + (3 * 10 ** mini if mini >= 0 else 0)
    #
    # def maximum69Number(self, num: int) -> int:
    #     l = list(str(num))
    #
    #     for i in range(len(l)):
    #         if l[i] == '6':
    #             l[i] = '9'
    #             break
    #
    #     return int(''.join(l))

    def maximum69Number(self, num: int) -> int:
        # pythonic
        return int(str(num).replace("6", "9", 1))
