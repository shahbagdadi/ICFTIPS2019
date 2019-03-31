# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_BST(root, lc, rc):

    # Base condition
    if root is None:
        return True

    if lc is not None and lc.data > root.data:
        return False

    if rc is not None and rc.data < root.data:
        return False

    return is_BST(root.left, lc, root ) and is_BST(root.right, root, rc)


def main():
    root = Node(40)
    root.left = Node(30)
    root.right = Node(50)
    root.left.left = Node(25)
    root.left.right = Node(35)
    root.right.left = Node(45)
    root.right.right = Node(55)

    if is_BST(root, None, None):
        print("Given tree is a BST")
    else:
        print("Given tree is NOT a BST")

if __name__ == '__main__':
  main()