# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time. Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        # self.min_val = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Checking if the min_val is None for initial case and if the min
        # list is empty

        # if self.min_val == None or val <= self.min_val:
        #   self.min_stack.append()
        #   self.min_val = val
        if self.min_stack == [] or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        #   Setting the min_val to None if the min list is empty to
        #   avoid comparing the min_val with further push op in list

        #   if self.min_stack == []
        #       self.min_val = None
        #   else:
        #       self.min_val = self.min_sack[-1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()