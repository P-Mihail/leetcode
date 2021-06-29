# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a
# chessboard for your reference.
#
# 8 [ ][x][ ][x][ ][x][ ][x]
# 7 [x][ ][x][ ][x][ ][x][ ]
# 6 [ ][x][ ][x][ ][x][ ][x]
# 5 [x][ ][x][ ][x][ ][x][ ]
# 4 [ ][x][ ][x][ ][x][ ][x]
# 3 [x][ ][x][ ][x][ ][x][ ]
# 2 [ ][x][ ][x][ ][x][ ][x]
# 1 [x][ ][x][ ][x][ ][x][ ]
#    a  b  c  d  e  f  g  h
#
# Return true if the square is white, and false if the square is black.
#
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and
# the number second.
#
# Example 1:
# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
#
# Example 2:
# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
#
# Example 3:
# Input: coordinates = "c7"
# Output: false
#
# Constraints:
# coordinates.length == 2
# 'a' <= coordinates[0] <= 'h'
# '1' <= coordinates[1] <= '8'


class Solution(object):
    def squareIsWhite(self, coordinates: str) -> bool:
        return (int(coordinates[1]) + (coordinates[0] in "bdfh")) % 2 == 0