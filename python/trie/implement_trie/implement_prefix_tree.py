
"""
A trie (pronounced as "try") or prefix tree is a tree data structure 
used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as 
autocomplete and spellchecker.

Implement the Trie class:
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in
    the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a 
    previously inserted string word that has the prefix prefix, and 
    false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

class TrieNode:

    def __init__(
            self, 
            key: str = None,
            on: bool = False,
            ):
        self.key = key
        self.on = on
        self.children = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(
            self, 
            word: str,
            ) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        i = 0
        prefix = str()
        while True:
            if prefix == word:
                root.on = True
                break
            if not len(root.children.keys()):
                root.children[word[i]] = TrieNode(word[i])
            if not word[i] in root.children.keys():
                root.children[word[i]] = TrieNode(word[i])
            prefix += root.children[word[i]].key
            root = root.children[word[i]]
            i += 1

    def search(
            self, 
            word: str,
            ) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not len(self.root.children):
            return False
        root = self.root
        i = 0
        while True:
            if i >= len(word):
                if root.on:
                    return True
                return False
            if word[i] not in root.children.keys():
                return False
            root = root.children[word[i]]
            i += 1

    def startswith(
            self, 
            prefix: str,
            ) -> bool:
        """
        Returns if there is any word in the trie that starts with the
        given prefix.
        """
        if not len(self.root.children):
            return False
        root = self.root
        i = 0
        while True:
            if i >= len(prefix):
                return True
            if prefix[i] not in root.children.keys():
                return False
            root = root.children[prefix[i]]
            i += 1
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
