from __future__ import annotations
from middle_linked_list import ListNode

# remove nth from end in a linked list


def remove(head: ListNode, n: int):
    length = 0
    curr_node = head
    while curr_node is not None:
        curr_node = curr_node.next
        length += 1

    curr_node = head
    prev_node = None
    next_node = curr_node.next
    for i in range(length - n):
        prev_node = curr_node
        curr_node = next_node
        next_node = curr_node.next

        if curr_node is None:
            break

    if prev_node is not None:
        prev_node.next = next_node
        return head

    return next_node


if __name__ == "__main__":
    assert remove(ListNode.build([1]), 1) == None
    assert str(remove(ListNode.build([1, 2]), 2)) == str(ListNode.build([2]))
    assert str(remove(ListNode.build([1, 2, 3, 4, 5]), 2)) == str(
        ListNode.build([1, 2, 3, 5]))
    assert str(remove(ListNode.build([1, 2]), 1)) == str(
        ListNode.build([1]))
