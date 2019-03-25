## Rebuild the tree!
Given the in-order and pre-order traversing results of a binary tree (as arrays), write a function to rebuild the tree.  
The function should return the pointer to the root node of the tree. Then take that pointer, and print your tree level by level (level order).  

Trivia: Generally speaking, one needs to be given in-order traversal (with either pre or post or level), as input, in order to re-construct a binary tree.  
Without in-order traversal given, it's not possible to re-construct a binary tree without ambiguity, even if all other 3 traversal orders are given.  
The only exception, is if we know something more about the tree e.g. if the binary tree is full and complete, then we can resolve the ambiguity without having to know the in-order traversal.  
   
http://www.geeksforgeeks.org/if-you-are-given-two-traversalsequences-can-you-construct-the-binary-tree/

``` 
For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```