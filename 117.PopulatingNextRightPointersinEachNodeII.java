// Queue
class Solution {
    public Node connect(Node root) {
        List<Node> q = new ArrayList<>();

        q.add(root);

        while (!q.isEmpty()){
            Node prev = null;
            int n = q.size();

            for (int i = 0; i < n; i++){
                Node curr = q.remove(q.size() - 1);
                if(curr != null){

                    curr.next = prev;
                    prev = curr;
                    if(curr.right != null){
                        q.add(0, curr.right);
                    }
                    if(curr.left != null){
                        q.add(0, curr.left);
                    }
                }
            }

        }

        return root; 
    }
}

// Space Optimized solution.
// We only move on to level N+1 when we are done establishing the next pointers for level N. So, since we have access to all the nodes on a particular level via the next pointers, we can use these next pointers to establish the connections for the next level or the level containing their children.
class Solution {
    public Node connect(Node root) {
        if (root == null){
            return root;
        }
        Node head = root;

        while (head != null){
            Node dummy = new Node(0);
            Node tmp = dummy;

            while (head != null){
                if(head.left != null){
                    tmp.next = head.left;
                    tmp = tmp.next;
                }

                if(head.right != null){
                    tmp.next = head.right;
                    tmp = tmp.next;
                }
                head = head.next;
            }
            head = dummy.next;
        }

        return root;
    }
}
