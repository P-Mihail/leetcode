# A robot on an infinite XY-plane starts at point (0, 0) and faces north. The robot can receive one of three possible
# types of commands:
#
# -2: turn left 90 degrees,
# -1: turn right 90 degrees, or
# 1 <= k <= 9: move forward k units.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi).
#
# If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues
# following the rest of the route.)
#
# Return the maximum Euclidean distance that the robot will be from the origin squared (i.e. if the distance is 5,
# return 25).
#
# Note:
#
# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.
#
#
# Example 1:
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point away from the origin is (3, 4), which is 32 + 42 = 25 units away.
#
# Example 2:
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
# 4. Turn left.
# 5. Move north 4 units to (1, 8).
# The furthest point away from the origin is (1, 8), which is 12 + 82 = 65 units away.
#
#
# Constraints:
# 1 <= commands.length <= 10^4
# commands[i] is one of the values in the list [-2,-1,1,2,3,4,5,6,7,8,9].
# 0 <= obstacles.length <= 10^4
# -3 * 10^4 <= xi, yi <= 3 * 10^4
# The answer is guaranteed to be less than 2^31.


from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = "NESW"
        right = {f: t for f, t in zip(d, d[1:] + d[0])}
        left = {f: t for f, t in zip(d, d[-1] + d[:-1])}
        obst = set([tuple(o) for o in obstacles])

        direction = "N"
        x, y, ans = 0, 0, 0

        for c in commands:
            if c == -2:
                direction = left[direction]
            elif c == -1:
                direction = right[direction]
            else:
                for _ in range(c):
                    if direction == "N":
                        if (x, y + 1) in obst:
                            break
                        y += 1
                    if direction == "S":
                        if (x, y - 1) in obst:
                            break
                        y -= 1
                    if direction == "E":
                        if (x + 1, y) in obst:
                            break
                        x += 1
                    if direction == "W":
                        if (x - 1, y) in obst:
                            break
                        x -= 1
                ans = max(ans, x ** 2 + y ** 2)

        return ans
