package sign_of_prod;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void testNums1Returns() {
        int[] nums1 = {-1, -2, -3, -4, 3, 2, 1};
        Solution sol = new Solution();
        assertTrue(sol.arraySign(nums1) == 1);
    }

    @Test
    public void testNums2Returns() {
        int[] nums2 = {1, 5, 0, 2, -3};
        Solution sol = new Solution();
        assertTrue(sol.arraySign(nums2) == 0);
    }

    @Test
    public void testNums3ReturnsNeg1() {
        int[] nums3 = {-1, 5, 3, 12, -51, 3, -3};
        Solution sol = new Solution();
        assertTrue(sol.arraySign(nums3) == -1);
    }

    @Test
    public void testNums4Returns() {
        int[] nums4 = {41, 65, 14, 80, 20, 10, 55, 58, 24, 56, 28, 86,
            96,10,3,84,4,41,13,32,42,43,83,78,82,70,15,-41};
        Solution sol = new Solution();
        System.out.println(sol.arraySign(nums4));
        assertTrue(sol.arraySign(nums4) == -1);
    }
}
