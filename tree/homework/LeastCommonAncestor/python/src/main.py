"""
Least Common Ancestor (LCA)

(Another popular interview problem)
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that has both n1 and n2 as descendants.
The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root.
Computation of lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs of nodes in a tree: the distance from n1 to n2 can be computed as the distance from the root to n1, plus the distance from the root to n2, minus twice the distance from the root to their lowest common ancestor. (Source: Wikipedia)
Design an write an algorithm to find the LCA node, given two nodes in a Binary Tree.

    The tree may or may not be a BST
    Assume a Node structure that has NO parent pointer
    Assume that the two nodes are distinct and exist in the tree
    Find a solution that has runtime complexity of O(N). N is # nodes in the tree.

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
"""

# T - O(?) where ? is ...O(h)
# S - O(?) where ? is ...O(h)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, p, q):

    # Base condition
    if root is None:
        return None

    # if p and q are greater than root data then LCA lies in right of the root node
    if root.data < p and root.data < q:
        return lca(root.right, p, q)

    # if p and q are lesser than root data then LCA lies in left of the root node
    if root.data > p and root.data > q:
        return lca(root.left, p, q)

    return root


def main():

    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.left.left.left = Node(None)
    root.left.left.right = Node(None)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)

    # scenario 1
    p = 5
    q = 1
    result = lca(root, p, q)
    print(f"LCA of p={p} and q={q} is {result.data}")

    # scenario 2
    p = 5
    q = 4
    result = lca(root, p, q)
    print(f"LCA of p={p} and q={q} is {result.data}")

if __name__ == '__main__':
  main()