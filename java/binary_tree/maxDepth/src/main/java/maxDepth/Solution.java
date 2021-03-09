package maxDepth;

class Solution {

    public int maxDepth(TreeNode root) {
        if (root == null) {return 0;} 
        if (root.left == null && root.right == null) {
            return 1;
        }
        int depthLeft = maxDepth(root.left);
        int depthRight = maxDepth(root.right);
        return 1 + Math.max(depthLeft, depthRight);
    }

    

}
