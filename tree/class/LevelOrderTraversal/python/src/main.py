"""
Given a binary tree, print the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

print its level order traversal as:
 3 9 20 15 7
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
        return None

    if root:

        print_inorder_tree(root.left)
        print(root.data, '->', end=' ')
        print_inorder_tree(root.right)

def print_leverl_order_tree(root):

    if root is None:
        return None

    queue = []
    queue.append(root)

    while len(queue) > 0:

        print(queue[0].data, end=' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def main():
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print("print binary tree using inorder traversal")
    print(print_inorder_tree(root))

    print("print level order binary tree")
    print_leverl_order_tree(root)

if __name__ == '__main__':
  main()