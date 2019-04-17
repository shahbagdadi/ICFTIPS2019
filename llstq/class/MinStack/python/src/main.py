"""
Minimum Stack

Design a stack that supports push, pop and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.

getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();

minStack.getMin();   --> Returns -2.

"""

# T - O(?) where ? is ... O(1)
# S - O(?) where ? is ... O(n)

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def peek(self):
        if self.stack:
            return self.stack[-1]


class MinStack:

    def __init__(self):
        self.val = Stack()
        self.min = Stack()

    def push(self, i):

        if self.min.is_empty() or self.min.peek() > i:
            self.min.push(i)

        self.val.push(i)

    def pop(self):

        val = self.min.pop()

        if val == self.min.peek():
            self.min.pop()

        return val

    def peek(self):
        return self.val.peek()

    def get_min(self):
        return self.min.peek()

def main():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())
    # --> Returns - 3
    min_stack.pop()

    print(min_stack.get_min())
    # --> Returns - 2


if __name__ == '__main__':
  main()