# https://leetcode.com/problems/implement-queue-using-stacks/

class Queue(object):

    # simulating first a stack
    class Stack():
        def __init__(self):
            self.stack_list = []
        def push(self, x):
            self.stack_list.append(x)
        def pop(self):
            return self.stack_list.pop()
        def peek(self):
            return self.stack_list[-1]
        def empty(self):
            return True if not self.stack_list else False

    def __init__(self):
        """
        initialize your data structure here.
        """
        # considering the stack top value as the oldest element in the queue
        # pop fast: O(1); push slow: O(n)
        self.stack = self.Stack()
        self.stack_tmp = self.Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while not self.stack.empty():
            self.stack_tmp.push(self.stack.pop())
        self.stack.push(x)
        while not self.stack_tmp.empty():
            self.stack.push(self.stack_tmp.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.empty()