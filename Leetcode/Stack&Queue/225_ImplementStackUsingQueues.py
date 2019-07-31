"""
author: buppter
datetime: 2019/7/31 11:09

题目描述：
用队列实现栈

解题思路：
用两个队列，一个实现入栈，一个实现出栈
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_queue = []
        self.pop_queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.push_queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.push_queue) != 1:
            self.pop_queue.append(self.push_queue.pop(0))
        self.push_queue, self.pop_queue = self.pop_queue, self.push_queue
        return self.pop_queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.push_queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.push_queue or self.pop_queue:
            return False
        return True


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    # em = s.pop()
    print(s.top())
    print(s.pop())
    print(s.empty())

