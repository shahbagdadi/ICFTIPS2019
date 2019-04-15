"""
Cycle in a linked List

Given a LinkedList find if there is a cycle in the linked list.

A --> B --> C --> D --> E --> F
                  |           |
                  K           G
                  |           |
                  J <-- I <-- H

The above should return true.

Follow up Question : Find the node where the cycle begins.
"""

# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(1)

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

    def print_list(self):

        current = self.head

        while current:
            print(current.data, '->', end=' ')
            current = current.next

    def create_loop(self):

        src = self.head.next.next.next.next.next.next.next.next.next.next
        print("source: ", src.data)
        dst = self.head.next.next.next
        print("destination: ", dst.data)
        src.next = dst

    def has_cycle(self):

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def main():
    lst = LinkedList()
    lst.add_element('K')
    lst.add_element('J')
    lst.add_element('I')
    lst.add_element('H')
    lst.add_element('G')
    lst.add_element('F')
    lst.add_element('E')
    lst.add_element('D')
    lst.add_element('C')
    lst.add_element('B')
    lst.add_element('A')

    print("print linked list")
    print(lst.print_list())

    # create a loop
    lst.create_loop()

    # detect a loop in a list
    print(lst.has_cycle())

if __name__ == '__main__':
  main()