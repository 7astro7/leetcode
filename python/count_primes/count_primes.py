
# Count the number of prime numbers LESS THAN a non-negative number, n.

# Example 1:
#   Input: n = 10
#   Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:
#   Input: n = 0
#   Output: 0
# Example 3:
#   Input: n = 1
#   Output: 0

# Constraints:
#    0 <= n <= 5 * 10**6

class Solution:

    def __init__(self):
        self.primes_map = dict()

    def _set_primes_map(self):
        for i in range(self.n):
            if i > 3:
                self.primes_map[i] = None 
            elif 2 <= i <= 3:
                self.primes_map[i] = True
            else:
                self.primes_map[i] = False

    def _check_preconditions(self):
        if not 0 <= self.n <= 5e6:
            raise Exception("!(0 <= n <= 5e6)")
    
    def _assign_evens(self):
        for i in range(self.n):
            if i > 2 and i % 2 == 0:
                self.primes_map[i] = False

    def _get_multiples(self, an_int: int):
        i = 2
        while an_int * i < self.n:
            a_composite = an_int * i
            self.primes_map[a_composite] = False
            i += 1

    def count_primes(self, n: int) -> int:
        self.n = n 
        self._check_preconditions()
        if self.n <= 1:
            return 0
        self._set_primes_map() 
        self._assign_evens()
        j = 2 
        while j < self.n:                
            if j % 2 == 0 and j != 2:
                j += 1
            self._get_multiples(j) 
            key_exists = j in self.primes_map.keys() 
            if key_exists and self.primes_map[j] is None:
                self.primes_map[j] = True
            j += 1
        return sum(self.primes_map.values())


n = 7920
sol = Solution()
print(sol.count_primes(n))
#print(sol.primes_map)

