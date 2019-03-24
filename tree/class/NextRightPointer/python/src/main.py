
# T - O(?)
# S - O(/) 
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.nextRight = None

def connectTree(cur):
   pass

def main():
    n20 = Node(20)
    n30 = Node(30)
    n40 = Node(40)
    n50 = Node(50)
    n60 = Node(60)
    n20.left = n30
    n20.right = n40
    connectTree(n20) 

if __name__ == "__main__":
    main()