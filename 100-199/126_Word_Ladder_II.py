# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
# beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences
# from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
#
#
#
# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
#
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#
# Constraints:
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 1000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


from typing import List
from collections import defaultdict


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def adj(s: str) -> List[str]:
            ans = []
            for i in range(len(s)):
                ans.append(s[:i] + "*" + s[i + 1 :])
            return ans

        hm1 = defaultdict(list)
        hm2 = defaultdict(list)

        for w in wordList:
            tmp = adj(w)
            hm1[w] = tmp
            for a in tmp:
                hm2[a].append(w)

        routes = (
            [[beginWord]]
            if beginWord in hm1
            else [[beginWord] + x for x in [hm2[x] for x in adj(beginWord) if x in hm2]]
        )
        used_w = set(x[0] for x in routes)

        while endWord not in used_w and len(routes) > 0:
            new_used_w = set()
            new_routes = []
            for route in routes:
                for a in hm1[route[-1]]:
                    for nw in hm2[a]:
                        if nw == endWord or nw not in used_w:
                            new_routes.append(route + [nw])
                            new_used_w.add(nw)
            routes = new_routes
            used_w |= new_used_w

        return [r for r in routes if r[-1] == endWord]
