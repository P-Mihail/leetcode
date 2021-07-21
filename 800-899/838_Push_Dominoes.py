# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push
# some of the dominoes either to the left or to the right.
#
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the
# dominoes falling to the right push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or
# already fallen domino.
#
# You are given a string dominoes representing the initial state where:
#
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
#
#
# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
#
# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#
#
# Constraints:
# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] is either 'L', 'R', or '.'.


class Solution:
    class Solution:
        def pushDominoes(self, dominoes: str) -> str:
            r = []
            ans = list(dominoes)

            t = -1
            for d in ans:
                if t >= 0:
                    t += 1

                if d == "R":
                    t = 0
                elif d == "L":
                    t = -1

                r.append(t)

            t = -1
            for i in range(len(dominoes) - 1, -1, -1):
                if t >= 0:
                    t += 1

                if ans[i] == "L":
                    t = 0
                elif ans[i] == "R":
                    t = -1

                if t == r[i]:
                    continue
                elif t == -1:
                    ans[i] = "R"
                elif r[i] == -1:
                    ans[i] = "L"
                else:
                    ans[i] = "L" if t < r[i] else "R"

            return "".join(ans)
