"""
Identical Tree

Given 2 Trees with their root node , return true if both trees are identical.
"""

# T - O(?) where ? is ...O(h)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_trees_identical(node1, node2):

    # Base condition
    if node1 is None and node2 is None:
        return True

    # if node1 is not None and node2 is not None and node1.data == node2.data:
    #     return is_identical(node1.left, node2.left)

    # if node1 is not None and node2 is not None and node1.data == node2.data:
    #     return is_identical(node1.right, node2.right)

    if node1 is not None and node2 is not None and node1.data == node2.data:
        return is_trees_identical(node1.left, node2.left) and is_trees_identical(node1.right, node2.right)

    return False



def main():

    # node1 tree
    node1 = Node(3)
    node1.left = Node(5)
    node1.right = Node(1)
    node1.left.left = Node(6)
    node1.left.right = Node(2)
    node1.right.left = Node(0)
    node1.right.right = Node(8)

    # node2 tree
    node2 = Node(3)
    node2.left = Node(5)
    node2.right = Node(1)
    node2.left.left = Node(6)
    node2.left.right = Node(2)
    node2.right.left = Node(0)
    node2.right.right = Node(8)

    print(is_trees_identical(node1, node2))


if __name__ == '__main__':
  main()