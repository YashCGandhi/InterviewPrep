class Solution {
    TreeNode prev;
    int diff = Integer.MAX_VALUE;

    public void inorder(TreeNode node){
        if (node == null){
            return;
        }
        inorder(node.left);
        if (prev != null){
            diff = Math.min(diff, node.val - prev.val);
        }
        prev = node;
        inorder(node.right);
    }

    public int getMinimumDifference(TreeNode root) {
        
        inorder(root);

        return diff;
        
    }
}
