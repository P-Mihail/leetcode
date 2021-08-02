# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not
# banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
#
#
# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
#
# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"
#
#
# Constraints:
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.


from typing import Dict, List
from collections import defaultdict

# from collections import Counter


class Solution:
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     return Counter(
    #         w
    #         for w in "".join(
    #             ch.lower() if ch.isalpha() else " " for ch in paragraph
    #         ).split()
    #         if w not in set(banned)
    #     ).most_common(1)[0][0]

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # time complexity O(m + n)
        # space complexity O(m + n)
        # m - number of characters in the banned list, n - number of characters in the input string
        setbanned = set(banned)

        c: Dict[str, int] = defaultdict(int)
        ans = ""
        mcount = 0

        ps = pe = 0
        while ps < len(paragraph):
            pe = ps + 1
            if paragraph[ps].isalpha():
                while pe < len(paragraph) and paragraph[pe].isalpha():
                    pe += 1
                word = paragraph[ps:pe].lower()
                if word not in setbanned:
                    c[word] += 1
                    if c[word] > mcount:
                        mcount += 1
                        ans = word
            ps = pe
        return ans
