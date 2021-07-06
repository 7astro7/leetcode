
package majority_element;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class SolutionTest {

	@Test
	public void testNums1Returns3() {
		int[] nums1 = {3, 2, 3};
		Solution sol = new Solution();
		assertTrue(sol.majorityElement(nums1) == 3);
	}

	@Test
	public void testNums2Returns2() {
		int[] nums2 = {2, 2, 1, 1, 1, 2, 2};
		Solution sol = new Solution();
		assertTrue(sol.majorityElement(nums2) == 2);
	}

	@Test
	public void testNums3Returns9() {
		int[] nums3 = {98, 9, 9, 9, 9, 3, 3, 9, 9, 9, 3, 3};
		Solution sol = new Solution();
		assertTrue(sol.majorityElement(nums3) == 9);
	}

}

