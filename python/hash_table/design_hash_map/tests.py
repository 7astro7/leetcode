
import numpy as np
import unittest
from design_hash_map import MyHashMap

class TestMyHashMap(unittest.TestCase):

    def get_pareto_ints(self, mode: float, 
            alpha: float = 11 / 10) -> map:
        generator = np.random.default_rng()
        pareto = (generator.pareto(alpha, int(1e4)) + 1) * mode
        for num in pareto:
            yield int(num)

    def get_uniform_ints(self, 
            rng: range = range(0, int(1e6), int(1e4))) -> map:
        generator = np.random.default_rng()
        uniform_floats = generator.uniform(rng)
        for num in uniform_floats:
            yield int(num)

    def test_map_k0_to_v1_get43_returns_neg1(self):
        hash_map = MyHashMap()
        hash_map.put(key = 0, value = 1)
        self.assertEqual(hash_map.get(43), -1)

    def test_map_k0_to_v1_get0_returns1(self):
        hash_map = MyHashMap()
        hash_map.put(key = 0, value = 1)
        self.assertEqual(hash_map.get(0), 1)

    def test_add_and_remove_5k_kv_pairs_getk_returns_neg1(self):
        hash_map, observed = MyHashMap(), []
        rand_keys = tuple(self.get_uniform_ints())
        rand_values = tuple(self.get_uniform_ints())
        expected = list(zip(rand_values, (-1,) * int(5e3)))
        for k, v in zip(rand_keys, rand_values):
            hash_map.put(key = k, value = v)
            pre_remove = hash_map.get(k)
            hash_map.remove(k)
            post_remove = hash_map.get(k)
            observed.append((pre_remove, post_remove,))
        self.assertEqual(expected, observed)

    def test_get_works_up_to_1million(self):
        hash_map, observed = MyHashMap(), []
        i = int(999e3)
        neg1 = (-1,) * int(1e4)
        expected = list(zip(range(int(999e3), int(1e6 + 1)), neg1))
        while i < int(1e6 + 1):
            hash_map.put(key = i, value = i)
            get_pre_remove = hash_map.get(i)
            hash_map.remove(i)
            get_post_remove = hash_map.get(i)
            observed.append((get_pre_remove, get_post_remove,))
            i += 1
        self.assertEqual(expected, observed)

    def test_get_works_up_to_1million_no_remove(self):
        hash_map = MyHashMap()
        rng = range(int(999e3), int(1e6 + 1))
        for i in rng:
            hash_map.put(key = i, value = i)
        get_get_result = lambda key: hash_map.get(key)
        observed = tuple(map(get_get_result, rng))
        self.assertEqual(tuple(rng), observed)

    def test_get_works_for_pareto_shape2_mode1e2(self):
        hash_map, observed = MyHashMap(), []
        keys = tuple(self.get_pareto_ints(alpha = 2, mode = 1e2))
        values = tuple(self.get_pareto_ints(alpha = 2, mode = 1e2))
        expected = list(zip(values, (-1,) * int(1e4)))
        for k, v in zip(keys, values):
            hash_map.put(key = k, value = v)
            pre_remove = hash_map.get(k)
            hash_map.remove(k)
            post_remove = hash_map.get(k)
            observed.append((pre_remove, post_remove,))
        self.assertEqual(expected, observed)


if __name__ == "__main__":
    unittest.main()
