
import pytest
from swap_nodes_in_pairs import Solution
from ListNode import ListNode

@pytest.fixture
def sol():
    return Solution()

@pytest.fixture
def node_value_1():
    return ListNode(1)

@pytest.fixture
def head_of_pair_of_nodes():
    head = ListNode(100)
    head.next = ListNode(99)
    return head

@pytest.fixture
def head_of_list_with_vals_1_through_4():
    lst = tuple(ListNode(i) for i in range(1, 5))
    for i in range(len(lst) - 1):
        lst[i].next = lst[i + 1]
    return lst[0]

@pytest.fixture
def head_of_list_with_vals_0_through_100():
    lst = tuple(ListNode(i) for i in range(101))
    for i in range(len(lst) - 1):
        lst[i].next = lst[i + 1]
    return lst[0]

def test_list_size_101(
        sol: Solution, 
        head_of_list_with_vals_0_through_100: ListNode
        ):
    head_node = head_of_list_with_vals_0_through_100
    node_after_head = head_node.next
    assert sol.swap_pairs(head_node) == node_after_head

# works
def test_null_head_returns_empty_list(sol: Solution):
    assert sol.swap_pairs(None) == None

# works
def test_node_value_1_returns_1(
        sol: Solution,
        node_value_1: ListNode
        ):
#    breakpoint()
    assert sol.swap_pairs(node_value_1) == node_value_1

# works
def test_two_node_swap(sol: Solution, head_of_pair_of_nodes: ListNode):
    head_node = head_of_pair_of_nodes
    node_after_head = head_node.next
    assert sol.swap_pairs(head_node) == node_after_head

def test_head_of_list_with_vals_1_through_4_returns_2(
        sol: Solution,
        head_of_list_with_vals_1_through_4: ListNode
        ):
    head_node = head_of_list_with_vals_1_through_4
    node_after_head = head_node.next
#    breakpoint()
    assert sol.swap_pairs(head_node) == node_after_head


