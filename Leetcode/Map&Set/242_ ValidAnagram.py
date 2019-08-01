"""
author: buppter
datetime: 2019/7/31 15:41

题目描述：
有效的字母异位词
Given two strings s and t , write a function to determine if t is an anagram of s.

示例：
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

解题思路：
利用 Map 统计每个字母出现次数，然后做比较
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1

        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
        return dict1 == dict2
