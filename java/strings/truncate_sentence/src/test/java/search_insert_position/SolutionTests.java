
package truncate_sentence;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class SolutionTests {

	private boolean stringsMatch(String observed, String expected) {
		if (observed.length() != expected.length()) {
			return false;
		}
		for (int i = 0; i < observed.length(); i++) {
			if (observed.charAt(i) != expected.charAt(i)) {
				return false;
			}
		}
		return true;
	}

	@Test
	public void tests1k4() {
		Solution sol = new Solution();
		String s = "Hello how are you Contestant";
		String expected = "Hello how are you";
		String observed = sol.truncateSentence(s, 4);
		assertTrue(stringsMatch(observed, expected));
	}

	@Test
	public void tests2k4() {
		Solution sol = new Solution();
		String s = "What is the solution to this problem";
		String expected = "What is the solution";
		String observed = sol.truncateSentence(s, 4);
		assertTrue(stringsMatch(observed, expected));
	}

	@Test
	public void tests3k5() {
		Solution sol = new Solution();
		String s = "Christopher Columbus was from a city in Italy";
		String expected = "Christopher Columbus was from a";
		String observed = sol.truncateSentence(s, 5);
		assertTrue(stringsMatch(observed, expected));
	}
}
