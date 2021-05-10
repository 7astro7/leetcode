
import pytest
from implement_prefix_tree import Trie

@pytest.fixture
def trie() -> Trie:
    return Trie()

@pytest.fixture
def apple_trie(
        trie: Trie,
        ) -> Trie:
    trie.insert('apple')
    return trie

def test_0(
        trie: Trie,
        ):
    trie.insert('app')
    assert trie.search('app')

def test_apple_trie_search_apple_returns_true(
        apple_trie: Trie,
        ):
    assert apple_trie.search('apple')

def test_apple_trie_search_app_returns_false(
        apple_trie: Trie,
        ):
    assert not apple_trie.search('app')

def test_apple_trie_startswith_app_returns_true(
        apple_trie: Trie,
        ):
    assert apple_trie.startswith('app')

def test_apple_trie_insert_app_search_app_returns_true(
        apple_trie: Trie,
        ):
    apple_trie.insert('app')
    assert apple_trie.search('app')

@pytest.fixture
def trie2() -> Trie:
    trie2 = Trie()
    trie2.insert('millennium')
    return trie2

def test_trie2_insert(
        trie2: Trie,
        ):
    assert trie2.search('millennium')
    assert not trie2.search('mill')
    assert trie2.startswith('mill')
    trie2.insert('mill')
    assert trie2.search('mill')
    assert not trie2.search('newspaper')


