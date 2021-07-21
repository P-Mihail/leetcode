# Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all
# strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4
# times, you need to include that character three times in the final answer.
#
# You may return the answer in any order.
#
#
# Example 1:
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
#
# Example 2:
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
#
# Note:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


from typing import List
# from collections import Counter


class Solution:
    # def commonChars(self, words: List[str]) -> List[str]:
    #     counter = Counter(words[0])
    #
    #     for w in words[1:]:
    #         c = Counter(w)
    #         keys = list(counter.keys())
    #         for ch in keys:
    #             if c[ch] == 0:
    #                 counter.pop(ch)
    #             else:
    #                 counter[ch] = min(counter[ch], c[ch])
    #
    #     ans = []
    #     for ch in counter:
    #         ans += [ch] * counter[ch]
    #
    #     return list(ans)

    def commonChars(self, words: List[str]) -> List[str]:
        res: List[str] = []
        for ch in set(words[0]):
            count = []
            for word in words:
                count.append(word.count(ch))
            res += ch * min(count)
        return res
