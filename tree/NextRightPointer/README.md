# Tree Next right pointer

```
Given a binary tree

class Node {
  Node left;
  Node right;
  Node nextRight;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.



Given the following binary tree,

        20
      /    \
     30     40
    / \     / \
  50   60  70  80
      /     \
    90      99

After calling your function, the tree should look like:

        20 --> NULL
      /    \
     30 --> 40 --> NULL
    / \     / \
   50->60->70->80 --> NULL
      /     \
    90  --> 99 --> NULL
```

