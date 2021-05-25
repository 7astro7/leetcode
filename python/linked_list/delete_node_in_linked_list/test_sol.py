
import pytest
from delete_node_in_ll import Solution, ListNode

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_delete_head(
        sol: Solution,
        ):
    # -3 -> 5 -> -99
    neg3 = ListNode(-3) 
    five = ListNode(5)
    neg99 = ListNode(-99)
    neg3.next = five
    five.next = neg99
    sol.delete_node(neg3)
    # 5 -> -99
    assert neg3.next == neg99
    assert five.next == neg99

def test_4_5_1_9_delete_5(
        sol: Solution,
        ):
    # 4 -> 5 -> 1 -> 9
    four = ListNode(4) 
    five = ListNode(5)
    one = ListNode(1)
    nine = ListNode(9)
    four.next = five
    five.next = one
    one.next = nine
    sol.delete_node(five)
    # 4 -> 1 -> 9
    assert one.next == nine
    assert four.next.val == 1
    assert five.val == 1
    assert five.next == nine

def test_0_1(
        sol: Solution,
        ):
    # 0 -> 1
    zero = ListNode(0)
    one = ListNode(1)
    zero.next = one
    sol.delete_node(zero)
    # 1
    assert zero.next is None
    assert one.next is None

    
