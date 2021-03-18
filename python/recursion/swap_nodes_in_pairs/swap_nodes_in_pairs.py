
# Given a linked list, swap every two adjacent nodes and return its head.

"""
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""
from ListNode import ListNode

class Solution:

    def swap_pairs(self, head: ListNode) -> ListNode:
        if (head is None or not head or head.val is None): 
            return 
        if head.next is None: 
            return head
        return self._permute_pair(head)

    def _permute_pair(self, old_head: ListNode) -> ListNode:
        """
        Reorder pair that begins with old_head and set its .next
        attribute to correct node
        Return old_head if at end of list
        """
        if old_head is None: 
            return 
        if old_head.next is None: 
            return old_head
        future_head = old_head.next
        old_head.next = self._permute_pair(future_head.next)
        future_head.next = old_head
        return future_head



