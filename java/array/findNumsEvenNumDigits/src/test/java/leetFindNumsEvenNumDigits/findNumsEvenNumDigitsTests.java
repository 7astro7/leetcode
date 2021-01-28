
package leetFindNumsEvenNumDigits;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class findNumsEvenNumDigitsTests {

    public static int getActualOutput(int[] an_array) {
        findNumsEvenNumDigits ans = new findNumsEvenNumDigits();
        return ans.findNumbers(an_array);
    }

    @Test 
    public void test_555_901_482_1771_returns_1() {
        int[] an_array = {555, 901, 482, 1771}; 
        assertTrue(getActualOutput(an_array) == 1);
    }

    @Test
    public void test_12_345_2_6_7896_returns_2() {
        int[] an_array = {12, 345, 2, 6, 7896};
        assertTrue(getActualOutput(an_array) == 2);
    }

    @Test
    public void test_500_1s_returns_0() {
        int[] an_array = new int[500];
        assertTrue(getActualOutput(an_array) == 0);
    }

    @Test
    public void test_500_98s_returns_500() {
        int[] an_array = new int[500];
        for (int i = 0; i < 500; i++) {
            an_array[i] = 98;
        }
        assertTrue(getActualOutput(an_array) == 500); 
    }
}
