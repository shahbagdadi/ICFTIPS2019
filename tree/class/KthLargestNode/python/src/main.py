"""
Given a BST , return the kth largest node

For example:
Given binary tree

    13
   / \
  9  20
    /  \
   15   27

if K= 5 , return 9
"""

# T - O(?) where ? is ...O(h+k)
# S - O(?) where ? is ...O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_inorder(root):

    if root is None:
        return None
    else:
        print_inorder(root.left)
        print(root.data, '->', end=' ')
        print_inorder(root.right)

def create_a_tree(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = create_a_tree(root.left, data)
    elif data > root.data:
        root.right = create_a_tree(root.right, data)

    return root

def kthLargestNode(root, k):

    c = [0]
    return kth_largest_node_helper(root, k, c)

def kth_largest_node_helper(root, k, c):

    if root is None:
        return None

    kth_largest_node_helper(root.right, k, c)
    c[0] += 1
    # print('c[0] =', c[0])

    if c[0] == k:
        # print("kth largest node", root.data)
        return root

    return kth_largest_node_helper(root.left, k, c)

def main():

    root = None
    root = create_a_tree(root, 13)
    create_a_tree(root, 9)
    create_a_tree(root, 20)
    create_a_tree(root, 15)
    create_a_tree(root, 27)

    print(print_inorder(root))
    k = 5
    kth_largest_node = kthLargestNode(root, k)

    print(f"{k}th largest node is : {kth_largest_node.data}")


    # for k in range(1, 6):
    #    kthLargestNode(root, k)

if __name__ == '__main__':
  main()