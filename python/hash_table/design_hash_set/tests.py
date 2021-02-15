
import unittest
import numpy as np
from design_hash_set import MyHashSet

class TestMyHashSet(unittest.TestCase):

    def get_observed(self, a_hash_set: MyHashSet, start: int, 
            stop: int, stride: int = 1) -> map:
        while start < stop:
            yield a_hash_set.contains(start)
            start += stride

    def test_idk(self):
        observed, hash_set = [], MyHashSet()
        hash_set.add(33033)
        observed.append(hash_set.contains(33033)) # 1
        add_to_set = (43907, 32233, 58636, 66409,)
        hash_set = self.add_vector_to_hash_set(add_to_set)
        hash_set.remove(27702) 
        hash_set.add(80882)
        hash_set.remove(12563)
        observed.append(hash_set.contains(75034)) # 0
        hash_set.add(32143)
        hash_set.remove(1111)
        observed.append(hash_set.contains(61699)) # 0
        self.assertEqual(observed, [1, 0, 0,])

    def test_contains_works_up_to_1million(self):
        hash_set = MyHashSet()
        i = start = 990_000
        while i < 1_000_001:
            hash_set.add(i) 
            i += 1
        nums = sum(self.get_observed(hash_set, start, int(1e6)))
        self.assertEqual(nums, int(1e4))

    def test_add_14_9999_times_remove_contains_returns_false(self):
        hash_set = MyHashSet()
        i = 0
        while True:
            if i > 10_000:
                break
            hash_set.add(14)
            i += 1
        hash_set.remove(14)
        self.assertEqual(hash_set.contains(14), False)

    def test_add_and_remove_5K_elements_contains_returns_0(self):
        random_ints = np.random.randint(0, 10_000, 5_000)
        observed, hash_set = [], MyHashSet()
        expected = [1,] * len(random_ints)
        for random_int in random_ints:
            hash_set.add(random_int)
            shouldbe_true = hash_set.contains(random_int)
            hash_set.remove(random_int)
            shouldbe_false = hash_set.contains(random_int)
            observed.append(shouldbe_true + shouldbe_false)
        self.assertEqual(expected, observed)

    def test_contains_works_four_times(self):
        hash_set, observed = MyHashSet(), []
        expected = [True, False,] * 2
        hash_set.add(12)
        hash_set.add(5)
        observed.append(hash_set.contains(12)) # 1
        observed.append(hash_set.contains(18)) # 0
        hash_set.add(5)
        observed.append(hash_set.contains(5)) # 1
        hash_set.remove(5)
        observed.append(hash_set.contains(5)) # 0
        self.assertEqual(observed, expected)

    def test_add12_add2_contains12_returns_true(self):
        hash_set = self.add_vector_to_hash_set((12, 2,))
        self.assertTrue(hash_set.contains(12))

    def test_remove_deletes_element_after_2_additions(self):
        hash_set = self.add_vector_to_hash_set((1, 2,))
        hash_set.remove(2)
        self.assertFalse(hash_set.contains(2))

    def test_contains_17_returns_false_after_add_17_remove_17(self):
        hash_set = MyHashSet()
        hash_set.add(17)
        hash_set.remove(17)
        self.assertFalse(hash_set.contains(17))

    def add_vector_to_hash_set(self, a_vector, 
                               hash_set = None) -> MyHashSet:
        if hash_set is None:
            hash_set = MyHashSet()
        i = 0
        while i < len(a_vector):
            hash_set.add(a_vector[i])
            i += 1
        return hash_set

if __name__ == "__main__":
    unittest.main()
