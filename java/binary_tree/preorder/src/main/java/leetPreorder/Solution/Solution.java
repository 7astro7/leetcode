package leetPreorder.Solution;
import java.util.List;
import java.util.ArrayList;
import leetPreorder.TreeNode.TreeNode;

public class Solution {

/**
 Given the root of a binary tree, return the preorder traversal 
 of its nodes' values.

 Constraints:
 The number of nodes in the tree is in the range [0, 100].
 -100 <= Node.val <= 100
*/

    //static List<Integer> visited = new ArrayList<>();
    List<Integer> visited;
    public Solution() {
        this.visited = new ArrayList<>();
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null || !(root.val >= -100 && root.val <= 100)) {
            return visited;
        }
        return helper(root);
    }


    public List<Integer> helper(TreeNode root) {
        if (root == null) {
            return null;
        }
        visited.add(root.val);
        helper(root.left);
        helper(root.right);
        return visited; 
    }
}
