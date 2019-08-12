"""
题目描述:
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））

思路：
定义一个单独存放最小值的 min_list，当执行 push 时，对比 push 的值与 min_list 的值
如果更小，则也同时 push 进 min_list

执行 pop 时，如果当前值跟 min_list 的最小值相等，则同时 pop
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack:
            # 如果min_stack为空，则直接放入
            self.min_stack.append(node)
        elif node < self.min():
            # 如果 node 比 min_stack 里的最小值还小，则push进min_stack
            self.min_stack.append(node)

    def pop(self):
        if not (self.stack and self.min_stack):
            return None
        if self.stack[-1] == self.min():
            # 如果 pop 的值跟 min_stack 最小值相等，则同时 pop
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

