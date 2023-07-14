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
    private TreeNode prev = null, first = null, second = null;

    public void inorder(TreeNode r){
        if (r == null){
            return;
        }

        inorder(r.left);

        if (prev!=null && r.val < prev.val){
            if (first == null){
                first = prev;
            }
            second = r;
        }
        prev = r;

        inorder(r.right);
    }
    public void recoverTree(TreeNode root) {
        if (root == null){
            return;
        }

        inorder(root);
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
}
