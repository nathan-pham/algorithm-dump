from typing import Optional
from middle_linked_list import ListNode


def merge_sorted_lists(list_a: Optional[ListNode], list_b: Optional[ListNode]):
    if list_a is None:
        return list_b

    if list_b is None:
        return list_a

    curr_a = list_a
    curr_b = list_b
    merged = ListNode(None)
    curr_merged = merged

    def get_val(node: Optional[ListNode]):
        if node is None:
            return None

        return node.val

    while curr_merged is not None:
        if curr_a is None or curr_b is None:
            curr_merged.next = curr_a or curr_b
            break

        if curr_a.val < curr_b.val:
            curr_merged.next = curr_a
            curr_a = curr_a.next
        else:
            curr_merged.next = curr_b
            curr_b = curr_b.next

        curr_merged = curr_merged.next

    return merged.next


if __name__ == "__main__":
    assert merge_sorted_lists(
        ListNode.build([1, 2, 4]),
        ListNode.build([1, 3, 4])
    ) == ListNode.build([1, 1, 2, 3, 4, 4])

    assert merge_sorted_lists(
        None,
        None
    ) == None

    assert merge_sorted_lists(
        None,
        ListNode.build([0])
    ) == ListNode.build([0])
