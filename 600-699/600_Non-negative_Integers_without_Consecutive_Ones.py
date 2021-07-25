# Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not
# contain consecutive ones.
#
#
# Example 1:
# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
#
# Example 2:
# Input: n = 1
# Output: 2
#
# Example 3:
# Input: n = 2
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 10^9


class Solution:
    def findIntegers(self, n: int) -> int:
        # fn - count of numbers with size of n in bin representation which satisfy the rule
        # for example: fn[3] = 5 => *** = {'000', '001', '010', '100', '101'}
        # fn[2] = 3 => ** = {'00', '01', '10'}
        # fn[6] = {'10****', '0*****'} = fn[4] + fn[5]
        # fn[0] is trick for loop to append 1 to result if max_n has '1' in last bit
        fn = [
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
            10946,
            17711,
            28657,
            46368,
            75025,
            121393,
            196418,
            317811,
            514229,
            832040,
            1346269,
        ]
        # another words fn is count of numbers which satisfy the rule and less then 2^n for n >= 1

        nstr = bin(n)[2:]
        p = nstr.find("11")
        tmp = list(nstr)
        if p >= 0:
            for i in range(p + 1, len(tmp)):
                tmp[i] = "10"[(i - p) % 2]

        max_n = "".join(tmp)
        # max_n - bin representation of max number that satisfy the rule
        # bin(n) = '10011010' -> max_n = '10010101'
        # bin(n) = '1100' -> max_n = '1010'

        # main idea:
        #  n = 154 = 10011010 -> max_n = 10010101 = 10000000 + 10000 + 100 + 1
        # 10000000 => {10000000} + {0*******} -> 1 + fn[7] = 35
        # 10000 => {10000} + {0****} - {00000} (just used in prev step) -> 1 + fn[4] - 1 = fn[4] = 8
        # 100 => {100} + {0**} - {000} -> fn[2] = 3
        # 1 or fn[0]
        # ans = 35 + 8 + 3 + 1 = 47

        ans = fn[len(max_n) - 1] + 1
        for i in range(2, len(max_n)):
            if max_n[i] == "1":
                ans += fn[len(max_n) - i - 1]

        return ans
