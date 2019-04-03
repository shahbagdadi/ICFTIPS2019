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

# T - O(?) where ? is ...
# S - O(?) where ? is ...

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_postorder(root):

    if root is None:
        return None

    print_postorder(root.left)
    print_postorder(root.right)
    print(root.data, '->', end=' ')

def iterative_postorder(root):

    pass

def main():
    # node1 tree
    node1 = Node(4)
    node1.left = Node(2)
    node1.right = Node(6)
    node1.left.left = Node(1)
    node1.left.right = Node(3)
    node1.right.left = Node(5)
    node1.right.right = Node(7)

    print(print_postorder(node1))

    print(iterative_postorder(node1))


if __name__ == '__main__':
  main()