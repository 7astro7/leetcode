
package determine_color_of_chessboard_square;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class SolutionTest {

	@Test
	public void testa1False() {
		Solution sol = new Solution();
		assertTrue(!sol.squareIsWhite("a1"));
	}

	@Test
	public void testa2True() {
		Solution sol = new Solution();
		assertTrue(sol.squareIsWhite("a2"));
	}

	@Test
	public void teste5False() {
		Solution sol = new Solution();
		assertTrue(!sol.squareIsWhite("e5"));
	}

	@Test
	public void testh8False() {
		Solution sol = new Solution();
		assertTrue(!sol.squareIsWhite("h8"));
	}

}
