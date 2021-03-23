package leetInorder;

import org.junit.Test;
import java.util.List;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

public class SolutionTests {

    public static boolean traversedOK(List<Integer> observed, 
            List<Integer> expected) {
       for (int i = 0; i < expected.size(); i++) {
           if (observed.get(i) - expected.get(i) != 0) {
               return false;
           }
       }
       return true;
    }

    public static List<Integer> getObserved(TreeNode aRoot) {
        Solution sol = new Solution();
        return sol.inorderTraversal(aRoot);
    }

    @Test
    public void test_null_root_returns_empty_list() {
        List<Integer> expected = new ArrayList<>();
        List<Integer> observed = getObserved(null);
        assertTrue(traversedOK(observed, expected));
    }

    @Test
    public void test_1_2_returns_2_1() {
        TreeNode aRoot = new TreeNode(1);
        aRoot.left = new TreeNode(2);
        List<Integer> expected = new ArrayList<>();
        expected.add(2); expected.add(1); 
        assertTrue(traversedOK(getObserved(aRoot), expected));
    }

    @Test
    public void test_1_returns_1() {
        TreeNode aRoot = new TreeNode(1);
        List<Integer> expected = new ArrayList<>();
        expected.add(0, 1); 
        assertTrue(traversedOK(getObserved(aRoot), expected));
    }

    @Test
    public void test_1_null_2_3_returns_1_3_2() {
        List<Integer> expected = new ArrayList<>();
        expected.add(0, 1); expected.add(1, 3); expected.add(2, 2); 
        List<TreeNode> nodes = new ArrayList<>();
        for (int i = 1; i < 4; i++) {
            nodes.add(new TreeNode(i));
        }
        nodes.get(0).right = nodes.get(1);
        nodes.get(1).left = nodes.get(2);
        assertTrue(traversedOK(getObserved(nodes.get(0)), expected));
    }

    @Test
    public void test_1_null_2_returns_1_2() {
        List<Integer> expected = new ArrayList<>();
        expected.add(1); expected.add(2); 
        TreeNode aRoot = new TreeNode(1);
        aRoot.right = new TreeNode(2);
        assertTrue(traversedOK(getObserved(aRoot), expected));
    }

}
