package maxDepth;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;
import org.junit.Test;

public class SolutionTests {

    public List<TreeNode> depth5Tree = new ArrayList<>();

    public int observed(TreeNode aRoot) {
        Solution sol = new Solution();
        return sol.maxDepth(aRoot);
    }

    public void makeDepth5Tree() {
        int[] nodeVals = {4, -100, -9, -52, -4};
        for (int i: nodeVals) {
            depth5Tree.add(new TreeNode(i));
        }
        for (int i = 0; i < depth5Tree.size() - 1; i++) {
            if (i % 2 == 0) { 
                depth5Tree.get(i).right = depth5Tree.get(i + 1);
            }
            else {
                depth5Tree.get(i).left = depth5Tree.get(i + 1);
            }
        }
    }
    
    @Test
    public void test_one_node_tree_returns_1() {
        TreeNode node9 = new TreeNode(9);
        assertTrue(observed(node9) == 1);
    }

    @Test
    public void test_empty_tree_returns_0() {
        assertTrue(observed(null) == 0);
    }

    @Test 
    public void test_root_of_2_node_tree_returns_2() {
        TreeNode rootOf2NodeTree = new TreeNode(-57, null, new TreeNode(-83));
        assertTrue(observed(rootOf2NodeTree) == 2);
    }

    @Test
    public void test_max_depth_5_works() {
        makeDepth5Tree();
        assertTrue(observed(depth5Tree.get(0)) == 5);
    }
}
