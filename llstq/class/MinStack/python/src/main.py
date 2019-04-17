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

    def print_stack(self):
        for i in range(len(self.stack)):
            print(self.stack[i])


class MinStack:

    def __init__(self):
        self.val = Stack()
        self.min = Stack()

    def push(self, i):

        if self.min.is_empty() or self.min.peek() > i:
            self.min.push(i)

        self.val.push(i)

    def pop(self):

        val = self.val.pop()

        if val == self.min.peek():
            self.min.pop()

        return val

    def peek(self):
        return self.val.peek()

    def get_min(self):
        return self.min.peek()

    def print_stack(self):
        self.min.print_stack()

def main():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print("pushed elements in min stack")
    min_stack.print_stack()
    print("get the min stack element")
    print(min_stack.get_min())
    # --> Returns - 3
    print("pop operation")
    min_stack.pop()
    print("remaining min stack elements")
    min_stack.print_stack()
    print("get the min stack element")
    print(min_stack.get_min())
    # --> Returns - 2

    print()

    print("another test case")
    min_stack1 = MinStack()
    min_stack1.push(-2)
    min_stack1.push(3)
    min_stack1.push(-7)
    min_stack1.push(-1)
    print("pushed elements in min stack")
    min_stack1.print_stack()
    print("get the min stack element")
    print(min_stack1.get_min())
    print("pop operation")
    min_stack1.pop()
    print("remaining min stack elements")
    min_stack1.print_stack()
    print("get the min stack element")
    print(min_stack1.get_min())

if __name__ == '__main__':
  main()