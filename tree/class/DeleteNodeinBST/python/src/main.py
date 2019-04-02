"""
Delete Node in BST

Delete the given node in a BST , maintaining its BST properties

           20
         /    \
        15    17
       /  \
      13  16

Deleting 20 should result in
          17
         /
        15
       /  \
      13  16
"""

# T - O(?) where ? is ... O(log n) if tree is balanced height of the tree; O(n) if tree is skewed
# S - O(?) where ? is ...

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_inodrdertree(root):

    if root is None:
        return None
    else:
        print_inodrdertree(root.left)
        print(root.data, '->', end=' ')
        print_inodrdertree(root.right)

def get_min(root):

    while root.left is not None:
        root = root.left
    return root.data

# min from right method
def delete_node_in_bst_min_from_right(root, data):

    if root is None:
        return None
    if data < root.data:
        root.left = delete_node_in_bst_min_from_right(root.left, data)
    elif data > root.data:
        root.right = delete_node_in_bst_min_from_right(root.right, data)
    elif root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    else:
        min_from_right = get_min(root.right)
        root.data = min_from_right
        root.right = delete_node_in_bst_min_from_right(root.right, root.data)
    return root

def get_max(root):

    while root.right is not None:
        root = root.right
    return root.data

# max from left method
def delete_node_in_bst_max_from_left(root, data):

    if root is None:
        return None
    if data < root.data:
        root.left = delete_node_in_bst_max_from_left(root.left, data)
    elif data > root.data:
        root.right = delete_node_in_bst_max_from_left(root.right, data)
    elif root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    else:
        max_from_left = get_max(root.left)
        root.data = max_from_left
        root.left = delete_node_in_bst_max_from_left(root.left, root.data)
    return root

def main():

    # node1 tree
    node1 = Node(20)
    node1.left = Node(15)
    node1.right = Node(17)
    node1.left.left = Node(13)
    node1.left.right = Node(16)

    print("Print a binary search tree by using inoder traversal before deleting a node: ")
    print(print_inodrdertree(node1))

    # deleting a root node (20) from a BST (min from right)
    delete_node_in_bst_min_from_right(node1, 20)

    print()

    print("Print a binary search tree by using inoder traversal after deleting a node")
    print("by using min from right method")
    print(print_inodrdertree(node1))

    # deleting a root node (20) from a BST (max from left)
    delete_node_in_bst_max_from_left(node1, 20)

    print()

    print("Print a binary search tree by using inoder traversal after deleting a node")
    print("by using max from  left method")
    print(print_inodrdertree(node1))


if __name__ == '__main__':
  main()