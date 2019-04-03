"""
Iterative Traversal

Write an inorder traversal of a tree without using recursion.

Given the following binary tree,

        4
      /    \
     2      6
    / \     / \
  1    3  5    7

The inorder traversal of this tree should print
1 2 3 4 5 6 7
"""

# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterative_inorder(root):

    curr = root
    stack = []
    complete = 0

    while not complete:

        if curr is not None:
            stack.append(curr)

            curr = curr.left

        else:

            if len(stack) > 0:

                curr = stack.pop()
                print(curr.data, '->', end=' ')

                curr = curr.right

            else:
                complete = 1


def main():
    # node1 tree
    node1 = Node(4)
    node1.left = Node(2)
    node1.right = Node(6)
    node1.left.left = Node(1)
    node1.left.right = Node(3)
    node1.right.left = Node(5)
    node1.right.right = Node(7)

    print(iterative_inorder(node1))

if __name__ == '__main__':
  main()