// T - O(?)
// S - O(?)

public class Main {

    public void traverse(Node n)
    {

    }

    public static void main(String[] args) {

        Main m = new Main();
        Node n4 = new Node(4);
        Node n2 = new Node(2);
        Node n6 = new Node(6);
        Node n1 = new Node(1);
        Node n3 = new Node(3);
        Node n5 = new Node(5);
        Node n7 = new Node(7);
        n4.left = n2; n4.right = n6;
        n2.left = n1; n2.right = n3;
        n6.left = n5; n6.right = n7;
        m.traverse(n4);
    }
}
