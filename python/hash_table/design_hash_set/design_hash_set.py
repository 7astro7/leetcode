
# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:
#    add(value): Insert a value into the HashSet.
#    contains(value) : Return whether the value exists in the HashSet or not.
#    remove(value): Remove a value in the HashSet. If the value does 
#    not exist in the HashSet, do nothing.

# Example:
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);
# hashSet.contains(2);    // returns true
# hashSet.remove(2);
# hashSet.contains(2);    // returns false (already removed)

# Note:
#    All values will be in the range of [0, 1000000].
#    The number of operations will be in the range of [1, 10000].
#    Please do not use the built-in HashSet library.

class MyHashSet:

    def __init__(self):
        self.__table = [None,] * int(1e6 + 1)

    def add(self, key: int) -> None:
        if not 0 <= key <= int(1e6):
            return
        self.__table[key] = 1

    def remove(self, key: int) -> None:
        if not 0 <= key <= int(1e6):
            return
        self.__table[key] = None

    def contains(self, key: int) -> bool:
        if not 0 <= key <= int(1e6):
            return False
        return self.__table[key] is not None


if __name__ == "__main__":
    MyHashSet()
