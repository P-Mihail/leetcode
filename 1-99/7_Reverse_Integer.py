# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Example 4:
# Input: x = 0
# Output: 0
#
#
# Constraints:
# -2^31 <= x <= 2^31 - 1


class Solution(object):
    # Clean solution with suggested assumption
    def reverse(self, x: int) -> int:
        positive = x > 0
        limits = [
            214748364,
            7 if positive else 8,
        ]  # 2**31 // 10 == (2**31 - 1) // 10 == 214748364

        x = abs(x)
        rev = 0

        while x != 0:
            pop = x % 10
            x //= 10

            if rev > limits[0] or (rev == limits[0] and pop > limits[1]):
                return 0

            rev = rev * 10 + pop

        return rev if positive else -rev
