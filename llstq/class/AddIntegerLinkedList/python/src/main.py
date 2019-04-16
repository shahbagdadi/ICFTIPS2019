"""
Add Integer Linked List

Given two Integers LinkedList and add them

L1 : 2->4->3
L2 : 5->6->4

Result : 7->0->8
"""

# T - O(?) where ? is ... O(max(m,n))
# S - O(?) where ? is ...O(m+n)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # function insert new node at beginning
    def add_element(self, element):

        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def add_element_last(self, element):

        new_node = Node(element)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):

        current = self.head

        while current:
            print(current.data, '->', end=' ')
            current = current.next

    def add_list(self, n1, n2):

        if n1 is None:
            return None

        if n2 is None:
            return None

        carry = 0

        head = None
        current = None

        while n1 is not None or n2 is not None:

            a = b = 0

            if n1 is not None:
                a = n1.data
                n1 = n1.next

            if n2 is not None:
                b = n2.data
                n2 = n2.next

            # print("a ", a)
            # print("b ", b)

            sum_var = a + b + carry

            value = sum_var % 10
            carry = sum_var // 10

            if head is None:
                head = Node(value)
                current = head
                # print(current.data)
            else:
                current.next = Node(value)
                current = current.next
                # print(current.data)

            if carry > 0:
                current.next = Node(carry)

        # curr = head
        # while curr:
        #     print(curr.data)
        #     curr = curr.next

        self.head = head


def main():
    lst1 = LinkedList()
    lst1.add_element_last(2)
    lst1.add_element_last(4)
    lst1.add_element_last(3)

    lst2 = LinkedList()
    lst2.add_element_last(5)
    lst2.add_element_last(6)
    lst2.add_element_last(4)

    print("print linked list 1")
    print(lst1.print_list())

    print("print linked list 2")
    print(lst2.print_list())

    # lst3 = LinkedList()
    # lst3.add_element_last(1)
    # lst3.add_element_last(2)
    # lst3.add_element_last(3)
    #
    # print("print resulted linked list 3")
    # print(lst3.print_list())

    lst4 = LinkedList()
    n1 = lst1.head
    n2 = lst2.head

    lst4.add_list(n1, n2)

    print("print resulted linked list 4")
    print(lst4.print_list())



if __name__ == '__main__':
  main()