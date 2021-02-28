package leetPostorder;
import static org.junit.Assert.assertTrue;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class SolutionTests {

    private static boolean traversedOK(List<Integer> observed, 
        List<Integer> expected) {
            for (int i = 0; i < expected.size(); i++) {
                if (observed.get(i) - expected.get(i) != 0) {
                    return false;
                }
            }
            return true;
    }

    private static List<Integer> getObserved(TreeNode aRoot) {
        Solution sol = new Solution();
        return sol.postorderTraversal(aRoot);
    }

    @Test
    public void test_null_root_returns_empty_list() {
        List<Integer> observed = getObserved(null);
        assertTrue(traversedOK(observed, new ArrayList<>()));
    }

    @Test
    public void test_1_null_2_returns_2_1() {
        List<Integer> expected = new ArrayList<>();
        expected.add(2); expected.add(1);
        TreeNode aRoot = new TreeNode(1);
        aRoot.right = new TreeNode(2);
        List<Integer> observed = getObserved(aRoot);
        assertTrue(traversedOK(observed, expected));
    }

    @Test
    public void test_1_2_returns_2_1() {
        List<Integer> expected = new ArrayList<>();
        expected.add(2); expected.add(1);
        TreeNode aRoot = new TreeNode(1);
        aRoot.left = new TreeNode(2);
        List<Integer> observed = getObserved(aRoot);
        assertTrue(traversedOK(observed, expected));
    }

    @Test
    public void test_1_returns_1() {
        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        List<Integer> observed = getObserved(new TreeNode(1));
        assertTrue(traversedOK(observed, expected));
    }

    @Test
    public void test_1_null_2_3_returns_3_2_1() {
        List<Integer> expected = new ArrayList<>();
        List<TreeNode> nodes = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
           nodes.add(new TreeNode(i)); 
        }
        nodes.get(0).right = nodes.get(1);
        nodes.get(1).left = nodes.get(2);
        List<Integer> observed = getObserved(nodes.get(0));
        assertTrue(traversedOK(observed, expected));
    }
}
