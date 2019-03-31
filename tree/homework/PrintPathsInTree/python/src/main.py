"""
Print all paths in a tree

(Facebook question) Given a binary tree, print out all of its root-to-leaf paths one per line.

   e.g. for a tree that's
     1
    / \
   2   3
  / \ / \
 4  5 6  7

  Print:
   1 2 4
   1 2 5
   1 3 6
   1 3 7

"""

# T - O(?) where ? is ...O(h)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_all_paths_in_tree(stack_arr, root):

    # Base condition
    if root is None:
        return

    stack_arr.append(root.data)

    if root.left is None and root.right is None:
        print(" ".join(str(i) for i in stack_arr))

    print_all_paths_in_tree(stack_arr, root.left)
    print_all_paths_in_tree(stack_arr, root.right)

    stack_arr.pop()


def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Printing all paths in a tree: ")
    print_all_paths_in_tree([], root)


if __name__ == '__main__':
  main()