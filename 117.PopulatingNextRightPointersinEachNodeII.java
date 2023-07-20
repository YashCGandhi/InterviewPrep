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
