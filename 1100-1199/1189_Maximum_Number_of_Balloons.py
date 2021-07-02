# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as
# possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
# Example 1:
# Input: text = "nlaebolko"
# Output: 1
#
# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2
#
# Example 3:
# Input: text = "leetcode"
# Output: 0
#
# Constraints:
#
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.


from collections import Counter


class Solution:
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     # time complexity O(n)
    #     # space complexity O(1)
    #     count = Counter(text)
    #
    #     ht = {'a': 1,
    #           'b': 1,
    #           'l': 2,
    #           'n': 1,
    #           'o': 2, }
    #
    #     return min(count[c] // ht[c] for c in ht)

    def maxNumberOfBalloons(self, text: str) -> int:
        # without collections
        # time complexity O(n)
        # space complexity O(1)
        count = {c: 0 for c in 'ablno'}
        for c in text:
            if c in count:
                count[c] += 1

        ht = {'a': 1,
              'b': 1,
              'l': 2,
              'n': 1,
              'o': 2, }

        return min(count[c] // ht[c] for c in count)
