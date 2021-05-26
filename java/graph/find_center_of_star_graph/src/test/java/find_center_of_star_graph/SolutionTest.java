package find_center_of_star_graph;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class SolutionTest 
{
    private int observed(int[][] edges) {
        Solution sol = new Solution();
        return sol.findCenter(edges);
    }

    @Test
    public void testEdges1Returns2()
    {
        int[][] edges1 = {{2, 1}, {1, 2}, {2, 4}};
        assertTrue(observed(edges1) == 2);

    }

    @Test
    public void testEdges1Returns1()
    {
        int[][] edges2 = {{2, 1}, {1, 5}, {1, 3}, {1, 4}};
        assertTrue(observed(edges2) == 1);

    }

    @Test
    public void testEdges3Returns27()
    {
        int[][] edges3 = {{27, 8}, {12, 27}, {27, 4}, {27, 83}, 
            {27, 41}, {27, 26}, {27, 99}};
        assertTrue(observed(edges3) == 27);

    }

}
