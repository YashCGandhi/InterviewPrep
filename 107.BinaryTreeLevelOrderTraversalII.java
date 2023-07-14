/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        List<List<Integer>> tmp = new LinkedList<List<Integer>>();

        if (root == null){
            return tmp;
        }

        q.add(root);
        while(!q.isEmpty()){
            int n = q.size();

            List<Integer> current = new LinkedList<>();
            for (int i = 0; i < n; i++){
                TreeNode node = q.remove();
                current.add(node.val);
                if(node.left != null) q.add(node.left);
                if(node.right != null) q.add(node.right);
            }

            tmp.add(0, current);
        }
        return tmp;

    }
}
