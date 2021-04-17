#include <stdio.h>
#include <criterion/criterion.h>
#include <stdlib.h>

/*
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
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

Follow up: Can you solve the problem without modifying the values in the 
list's nodes? (i.e., Only nodes themselves may be changed.)
*/

/* From leetcode */
struct ListNode 
{
    int val;
    struct ListNode *next;
};

struct ListNode* permute_pair(struct ListNode* old_head) 
{
    if (!old_head || old_head == NULL)
        return old_head;
    if (!old_head->next || old_head->next == NULL)
        return old_head;
    struct ListNode *future_head = old_head->next;
    old_head->next = permute_pair(future_head->next);
    future_head->next = old_head;
    return future_head;
}

struct ListNode* swap_pairs(struct ListNode* head) 
{
    if (head == NULL || !head || !head->next) 
        return head;
    return permute_pair(head);
}

struct ListNode* make_node(void)
{
    struct ListNode* a_node = (struct ListNode*)malloc(sizeof(struct ListNode));
    return a_node;
}

Test(test_swap_nodes, node_value_1)
{
    struct ListNode *head = make_node();
    head->val = 1;
    struct ListNode *new_head = swap_pairs(head);
    cr_assert(new_head == head);
}

Test(test_swap_nodes, head_of_pair_of_nodes)
{
    struct ListNode *head = make_node();
    struct ListNode *after_head = make_node();
    head->val = 100;
    after_head->val = 99;
    head->next = after_head;
    struct ListNode *new_head = swap_pairs(head);
    cr_assert(new_head == after_head);
}

Test(test_swap_nodes, head_of_nodes_with_vals_1_through_4)
{
    struct ListNode *head = make_node();
    struct ListNode *after_head = make_node();
    struct ListNode *tail = make_node();
    head->val = 100;
    after_head->val = 99;
    tail->val = 98;
    head->next = after_head;
    after_head->next = tail;
    struct ListNode *new_head = swap_pairs(head);
    cr_assert(new_head == after_head);
}

