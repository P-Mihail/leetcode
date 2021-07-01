# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the
# minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the below binary watch reads "4:51".
#
# 8 [4] 2 1 [PM]
# [32] [16] 8 4 [2] [1]
#
# Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the
# watch could represent. You may return the answer in any order.
#
# The hour must not contain a leading zero.
#
# For example, "01:00" is not valid. It should be "1:00".
# The minute must be consist of two digits and may contain a leading zero.
#
# For example, "10:2" is not valid. It should be "10:02".
#
#
# Example 1:
#
# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:
#
# Input: turnedOn = 9
# Output: []
#
#
# Constraints:
#
# 0 <= turnedOn <= 10


from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        minutes = {
            1: 1,
            2: 2,
            4: 4,
            8: 8,
            16: 16,
            32: 32,
            64: 60,
            128: 120,
            256: 240,
            512: 480,
        }
        ans = []

        for i in range(2 ** turnedOn - 1, 764):  # int('0b1011111100',2)
            if i & 60 == 60:  # int('0b0000111100',2)
                continue
            c = 0
            time = 0
            for m in minutes:
                if i & m == m:
                    c += 1
                    if c > turnedOn:
                        break
                    time += minutes[m]
            if c == turnedOn:
                ans.append(f"{time // 60}:{time % 60:02d}")

        return ans
