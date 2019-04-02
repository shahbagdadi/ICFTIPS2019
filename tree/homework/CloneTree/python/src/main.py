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

def clone_a_tree(root):

    # Base condition
    if root is None:
        return None
    else:
        root2 = Node(root.data)
        root2.left = clone_a_tree(root.left)
        root2.right = clone_a_tree(root.right)

    return root2

def main():
    root = Node(6)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(7)
    root.left.right = Node(3)
    root.right.left = Node(8)
    root.right.right = Node(1)

    print("Print inorder traversal tree before cloning a tree: ")
    print_inorder_tree(root)
    print()
    print("Print inorder traversal tree after cloning a tree: ")
    print_inorder_tree(clone_a_tree(root))

if __name__ == '__main__':
  main()