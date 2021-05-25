package power_of_2;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

import org.junit.Test;

public class SolutionTest
{
    private boolean observed(int n) {
        Solution sol = new Solution();
        return sol.isPowerOfTwo(n);
    }

    @Test
    public void test1ReturnsTrue() {
        assertTrue(observed(1));
    }

    @Test
    public void test63ReturnsFalse() {
        assertFalse(observed(63));
    }

    public boolean powersOf2AllTrue() {
        for (int i = 0; i < 31; i++) {
            Double twoToI = Math.pow(2, i);
            int twoToIInt = twoToI.intValue();
            if (observed(twoToIInt) == false) {
                return false;
            }
        }
        return true;
    }

    @Test
    public void testPowersOf2ReturnsTrue() {
        assertTrue(powersOf2AllTrue());
    }

    public boolean notPowersOf2SampleAllFalse() {
        for (int i = 0; i < 31; i++) {
            Double notPow2 = -Math.pow(2, i);
            int notPow2Int = notPow2.intValue();
            if (observed(notPow2Int) == true) {
                System.out.println(notPow2Int);
                return false;
            }
        }
        return true;
    }

    @Test
    public void testNotPowersOf2SampleAllFalse() {
        assertTrue(notPowersOf2SampleAllFalse());
    }
}


