# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants
# represented by strings.
#
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between
# answers, output all of them with no order requirement. You could assume there always exists an answer.
#
#
# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines",
# "Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
#
# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
#
# Example 3:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express",
# "Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
#
# Example 4:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express",
# "Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
#
# Example 5:
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]
#
#
# Constraints:
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the stings of list1 are unique.
# All the stings of list2 are unique.


from typing import Dict, List


class Solution:
    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     # time complexity O(l1 + l2) не умножается на средний размер строки для взятия хэша т.к. ограничен сверху 30
    #     # space complexity O(l1)
    #     ht: Dict[str, int] = {}
    #
    #     for i, r in enumerate(list1):
    #         ht[r] = i
    #
    #     m = len(list1) + len(list2)
    #     ans = []
    #
    #     for i, r in enumerate(list2):
    #         if r in ht:
    #             if ht[r] + i == m:
    #                 ans.append(r)
    #             elif ht[r] + i < m:
    #                 ans = [r]
    #                 m = ht[r] + i
    #
    #     return ans

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # time complexity O(l1 + l2) не умножается на средний размер строки для взятия хэша т.к. ограничен сверху 30
        # space complexity O(l1 + l2)
        ht1: Dict[str, int] = {}

        for i, r in enumerate(list1):
            ht1[r] = i

        ht2: Dict[int, List[str]] = {}
        for i, r in enumerate(list2):
            if r in ht1:
                ht2[i + ht1[r]] = ht2.get(i + ht1[r], []) + [r]

        return ht2[min(ht2.keys())]
