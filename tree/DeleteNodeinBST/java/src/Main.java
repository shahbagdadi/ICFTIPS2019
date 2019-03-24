// T - O(?) where ? is ...
// S - O(?) where ? is ...

public class Main {

    public Node deleteNode(Node node, int data) {
        return null;
    }
    
    public static void main(String[] args) {
        Main m = new Main();
        Node r = new Node(20);
        Node n1 = new Node(15);
        Node n2 = new Node(17);
        Node n3 = new Node(13);
        r.left = n1;
        n1.right = n2;
        n1.left = n3;
        m.deleteNode(r,15);
    }
}