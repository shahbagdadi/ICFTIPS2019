"""
Flip a tree
   Reverse a general binary tree, i.e. flip it from right to left.
So for example if we had the binary tree
     6
    / \
   3   4
  / \ / \
 7  3 8  1

Reversing it would create
     6
    / \
   4   3
  / \ / \
 1  8 3  7

"""

# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_inorder_tree(root):

    if root is None:
        return
    else:
        print_inorder_tree(root.left)
        print(root.data, end=' ')
        print_inorder_tree(root.right)

def flip_a_tree(root):

    # Base condition
    if root is None:
        return None
    else:
        flip_a_tree(root.left)
        flip_a_tree(root.right)
        # swap the left and right nodes of a tree
        root.left, root.right = root.right, root.left

def main():
    root = Node(6)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(7)
    root.left.right = Node(3)
    root.right.left = Node(8)
    root.right.right = Node(1)

    print("Print inorder traversal tree before flipping a tree: ")
    print_inorder_tree(root)
    print()
    flip_a_tree(root)
    print("Print inorder traversal tree after flipping a tree: ")
    print_inorder_tree(root)

if __name__ == '__main__':
  main()