"""
Write a function to traverse a Binary tree PostOrder, without using recursion. As you traverse, please print contents of the nodes.
(Bonus: Spend 1 minute more and also do it with recursion)Given the following binary tree,

        4
      /    \
     2      6
    / \     / \
  1    3  5    7

The postorder traversal of this tree should print
1 3 2 5 7 6 4
"""

# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# postorder traversal using recursion
def print_postorder(root):

    if root is None:
        return None

    print_postorder(root.left)
    print_postorder(root.right)
    print(root.data, '->', end=' ')

# postorder traversal using two stacks
def iterative_postorder(root):

    if root is None:
        return None

    stack1 = []
    stack2 = []

    stack1.append(root)

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        current = stack2.pop()
        print(current.data, '->', end=' ')

def main():
    # node1 tree
    node1 = Node(4)
    node1.left = Node(2)
    node1.right = Node(6)
    node1.left.left = Node(1)
    node1.left.right = Node(3)
    node1.right.left = Node(5)
    node1.right.right = Node(7)

    print("Print postorder traversal of a binary tree using recursion")
    print(print_postorder(node1))

    print("Print postorder traversal of a binary tree w/o recursion and using two stacks")
    print(iterative_postorder(node1))

    print("Print postorder traversal of a binary tree w/o recursion and using one stack")
    # print(iterative_postorder_onestack(node1))


if __name__ == '__main__':
  main()