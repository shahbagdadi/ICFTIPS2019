"""
Valid Brackets

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
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

def is_balanced(str_var):

    if str_var is None or len(str_var) < 2:
        return False

    stack = Stack()

    for i in range(len(str_var)):

        ch = str_var[i]

        if ch == '[':
            stack.push(']')
        elif ch == '{':
            stack.push('}')
        elif ch == '(':
            stack.push(')')
        elif stack.is_empty() or stack.pop() != ch:
            return False

    return stack.is_empty()

def main():
    print("Valid Brackets for a given string of characters, return True or False")
    print("test case 1, input : ()")
    print(is_balanced("()"))
    print("test case 2, input : ()[]{}")
    print(is_balanced("()[]{}"))
    print("test case 3, input : (]")
    print(is_balanced("(]"))
    print("test case 4, input : ([)]")
    print(is_balanced("([)]"))


if __name__ == '__main__':
  main()