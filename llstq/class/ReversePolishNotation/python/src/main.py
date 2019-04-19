"""
Evaluate Reverse Polish Notation

Given a input ['2', '1', '+', '3', '*']
o/p : ((2+1) * 3) = 9
"""

# T - O(?) where ? is ...push, pop operations O(1)
# S - O(?) where ? is ... O(size of a stack)

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

def evaluate_reverse_polish_notation(str_var):

    if str_var is None or len(str_var) == 0:
        return 0

    stack = Stack()

    for i in range(len(str_var)):

        ch = str_var[i]

        if ch == '+':
            a = stack.pop()
            b = stack.pop()
            stack.push(a+b)
        elif ch == '-':
            a = stack.pop()
            b = stack.pop()
            stack.push(b-a)
        elif ch == '*':
            a = stack.pop()
            b = stack.pop()
            stack.push(a*b)
        elif ch == '/':
            a = stack.pop()
            b = stack.pop()
            stack.push(b/a)
        else:
            stack.push(int(ch))

    return stack.pop()

def main():
    print("Valid Brackets for a given string of characters, return True or False")
    print("test case 1, input : ['2', '1', '+', '3', '*']")
    print(evaluate_reverse_polish_notation(['2', '1', '+', '3', '*']))

if __name__ == '__main__':
  main()