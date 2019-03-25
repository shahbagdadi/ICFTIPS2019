## Convert a BST into a Circular Doubly Linked List
   
Write a recursive function treeToList(Node root) that takes a BST and rearranges the internal pointers to make a circular doubly linked list out of the tree nodes.  
The "previous" pointers should be stored in the "Left" field and the "next" pointers should be stored in the "Right" field.  
The list should be arranged so that the nodes are in increasing order.  
Return the head pointer to the new list. The operation can be done in O(n) time.

Let's take the following BST as an example, it may help you understand the problem better:

![BST](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png) 


 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 
![Circular List](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)  
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor.  
We should return the pointer to the first element of the linked list.




Suggested time: 45 minutes.
   
   