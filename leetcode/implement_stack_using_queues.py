# https://leetcode.com/problems/implement-stack-using-queues/

class Stack(object):

    # simulating first a stack
    class Queue():
        def __init__(self):
            self.queue_list = []
        def push(self, x):
            self.queue_list.append(x)
        def pop(self):
            return self.queue_list.pop(0)
        def peek(self):
            return self.queue_list[0]
        def empty(self):
            return True if not self.queue_list else False

    def __init__(self):
        """
        initialize your data structure here.
        """
        # considering the stack top value as the oldest element in the queue
        # pop fast: O(1); push slow: O(n)
        self.queue = self.Queue()
        self.queue_tmp = self.Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while not self.queue.empty():
            self.queue_tmp.push(self.queue.pop())
        self.queue.push(x)
        while not self.queue_tmp.empty():
            self.queue.push(self.queue_tmp.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.empty()