# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
#
# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
#
# Example 2:
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
#
# Example 3
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
#
# Constraints:
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8


from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]
        visited = {0}
        step = 0

        while curs:
            nex = []

            for node in curs:
                if node == n - 1:
                    return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
