# Implement the MapSum class:
#
# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original
# key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
#
#
# Example 1:
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]
#
# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
#
#
# Constraints:
# 1 <= key.length, prefix.length <= 50
# key and prefix consist of only lowercase English letters.
# 1 <= val <= 1000
# At most 50 calls will be made to insert and sum.

# Brute Force
# time complexity: insert - O(1), sum - O(N*P), N - number of items, P - prefix length
# class MapSum:
#     def __init__(self):
#         self.mem = {}
#
#     def insert(self, key: str, val: int) -> None:
#         self.mem[key] = val
#
#     def sum(self, prefix: str) -> int:
#         ans = 0
#
#         for k in self.mem:
#             if k.startswith(prefix):
#                 ans += self.mem[k]
#
#         return ans


# Tree based
# time complexity: insert - O(K), sum - O(K), K - length of key
class TreeNode:
    __slots__ = "children", "score"

    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum:
    def __init__(self):
        self.mem = {}
        self.root = TreeNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.mem.get(key, 0)
        self.mem[key] = val
        node = self.root
        node.score += delta
        for ch in key:
            node.children.setdefault(ch, TreeNode())
            node = node.children[ch]
            node.score += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return 0
        return node.score
