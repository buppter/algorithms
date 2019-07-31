"""
author: buppter
datetime: 2019/7/31 10:45

题目描述：
判断括号是否合法
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

示例：
Input: "()"
Output: true

Input: "([)]"
Output: false

解题思路：
利用栈
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i not in paren_map:
                stack.append(i)
            elif not stack or paren_map[i] != stack.pop():
                return False
        return not stack
