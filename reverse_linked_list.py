from typing import Optional
from middle_linked_list import ListNode


def reverse_linked_list(head: Optional[ListNode]):
    if head is None:
        return head

    # loop through to get the tail
    curr_node = head
    tail = curr_node
    while curr_node is not None:
        tail = curr_node
        curr_node = curr_node.next

    # start reversing the list
    prev_node, curr_node, next_node = None, head, None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return tail


if __name__ == "__main__":
    assert reverse_linked_list(
        ListNode.build([1, 2, 3, 4, 5])
    ) == ListNode.build([5, 4, 3, 2, 1])

    assert reverse_linked_list(
        ListNode.build([1, 2])
    ) == ListNode.build([2, 1])

    assert reverse_linked_list(
        None
    ) == None
