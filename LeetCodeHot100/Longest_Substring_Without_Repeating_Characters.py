"""
author: buppter
datetime: 2019/9/12 9:26
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub = []
        for i in s:
            if i not in sub:
                sub.append(i)
            else:
                max_len = max(max_len, len(sub))
                sub = sub[sub.index(i) + 1:]
                sub.append(i)
        return max(max_len, len(sub))
