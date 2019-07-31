"""
author: buppter
datetime: 2019/7/31 10:53

题目描述：
利用栈实现队列

解题思路：
两个栈，一个负责入，一个负责出
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.pop_stack:
            return self.pop_stack.pop()
        else:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.pop_stack:
            return self.pop_stack[-1]
        else:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.push_stack or self.pop_stack:
            return False
        return True
