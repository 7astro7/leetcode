package leetPreorder;
import static org.junit.Assert.assertTrue;
import java.util.ArrayList;
import java.util.List;
import org.junit.Test;
import leetPreorder.TreeNode.TreeNode;

public class SolutionTests {

    public static ArrayList<TreeNode> treeNodeVector(int[] nums) {
        ArrayList<TreeNode> tree = new ArrayList<TreeNode>();
        for (int i : nums) {
            tree.add(new TreeNode(i));
        }
        return tree;
    }

    public static boolean traversedOK(List<Integer> expected, 
        List<TreeNode> a_tree) {

        for (int i = 0; i < a_tree.size(); i++) {
            if (expected.get(i) - a_tree.get(i).val != 0) {
                return false;
            }
        }
        return true;
    }

    @Test
    public void test_empty_set_returns_empty_set() {
        List<Integer> expected = new ArrayList<>(); 
        List<TreeNode> tree = treeNodeVector(new int[0]);
        assertTrue(traversedOK(expected, tree));
    }

    @Test
    public void test_1null23_returns_123() {
        List<Integer> expected = new ArrayList<>(3); 
        expected.add(1); expected.add(2); expected.add(3); 
        List<TreeNode> tree = treeNodeVector(new int[] {1, 2, 3});
        tree.get(0).right = tree.get(1);
        tree.get(1).left = tree.get(tree.size() - 1);
        assertTrue(traversedOK(expected, tree));
    }

    @Test
    public void test_1_returns_1() {
        List<Integer> expected = new ArrayList<>(); 
        expected.add(1);
        List<TreeNode> tree = treeNodeVector(new int[] {1});
        assertTrue(traversedOK(expected, tree));
    }

    @Test
    public void test_1_null_2_returns_1_2() {
        List<Integer> expected = new ArrayList<>(); 
        expected.add(1); expected.add(2);
        List<TreeNode> tree = treeNodeVector(new int[] {1, 2});
        tree.get(0).right = tree.get(1);
        assertTrue(traversedOK(expected, tree));
    }

    @Test
    public void test_1_2_returns_1_2() {
        List<Integer> expected = new ArrayList<>(); 
        expected.add(1); expected.add(2);
        List<TreeNode> tree = treeNodeVector(new int[] {1, 2});
        tree.get(0).left = tree.get(1);
        assertTrue(traversedOK(expected, tree));
    }

    @Test
    public void test_only_left_children_size_5_returns() {
        int[] nums = {0, 5, 10, 15, 20, 25};
        List<TreeNode> tree = treeNodeVector(nums);
        List<Integer> expected = new ArrayList<>(); 
        int i = 0;
        while (i < 6) {
            if (i < 5) {
            tree.get(i).left = tree.get(i + 1);
            }
            expected.add(nums[i]);
            i++;
        }
        assertTrue(traversedOK(expected, tree));
    }

    @Test
    public void test_3_1_2_returns_3_1_2() {
        List<Integer> expected = new ArrayList<>(); 
        expected.add(3); expected.add(1); expected.add(2);
        List<TreeNode> tree = treeNodeVector(new int[] {3, 1, 2});
        tree.get(0).left = tree.get(1);
        tree.get(0).right = tree.get(2);
        assertTrue(traversedOK(expected, tree));
    }
}
