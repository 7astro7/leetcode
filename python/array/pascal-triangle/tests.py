
import unittest
from pascal_triangle import Solution
from make_pascal import MakePascal

class TestTriangle(unittest.TestCase):

    def test_1_row_returns_1(self):
        expected = MakePascal().get_triangle(1)
        self.assertEqual(expected, Solution().generate(1))

    def test_5_rows_returns_pascal(self):
        expected = MakePascal().get_triangle(5)
        self.assertEqual(expected, Solution().generate(5))

    def test_30_rows_returns_pascal(self):
        expected = MakePascal().get_triangle(30)
        self.assertEqual(expected, Solution().generate(30))


if __name__ == "__main__":
    unittest.main()
