
import unittest
from last_stone_weight import Solution

class TestLastStoneWeight(unittest.TestCase):

    stones1 = [2,7,4,1,8,1]
    stones2 = [434,667,378,919,212,902,240,257,208,996,411,222,557,
            634,425,949,755,833,785,886,40,159,932,157,764,916,85,
            300,130,278]

    def test_last_stone_weight_stones2_returns_1(self):
        solution = Solution().last_stone_weight(self.stones2)
        self.assertEqual(solution, 1)

    def test_last_stone_weight_stones1_returns_1(self):
        solution = Solution().last_stone_weight(self.stones1)
        self.assertEqual(solution, 1)

    def test_last_stone_weight_9_and_9_returns_0(self):
        solution = Solution().last_stone_weight([9,] * 2)
        self.assertEqual(solution, 0)

    def test_last_stone_weight_9_and_4_returns_5(self):
        solution = Solution().last_stone_weight([9, 4])
        self.assertEqual(solution, 5)

    def test_list_len31_raises_exception(self):
        with self.assertRaises(Exception):
            Solution().last_stone_weight([22,] * 31)

    def test_empty_list_raises_exception(self):
        with self.assertRaises(Exception):
            Solution().last_stone_weight([])

    def test_stones_with_stone_neg12_raises_value_error(self):
        with self.assertRaises(ValueError):
            Solution().last_stone_weight([-12, 45, 93])

    def test_stones_with_stone_10000_raises_value_error(self):
        with self.assertRaises(ValueError):
            Solution().last_stone_weight([10_000, 34, 2, 288])

if __name__ == "__main__":
    unittest.main()
