from __future__ import annotations
from typing import List, Union, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    @staticmethod
    def build(array: List[int]) -> Union[ListNode, None]:
        if len(array) == 0:
            return None

        head = ListNode(array[0], None)
        current_node = head
        for i in range(1, len(array)):
            current_node.next = ListNode(array[i])
            current_node = current_node.next

        return head

    def __str__(self):
        return f"[{self.val}, {str(self.next)}]"


def middle_node(head: Optional[ListNode] = None) -> Optional[ListNode]:
    if head is None:
        return None

    current_node: Optional[ListNode] = head
    nodes = []
    while current_node is not None:
        nodes.append(current_node)
        current_node = current_node.next

    return nodes[int((len(nodes) + 0.5) / 2)]


if __name__ == "__main__":
    assert str(middle_node(ListNode.build([1, 2, 3, 4, 5]))) == str(
        ListNode.build([3, 4, 5]))

    assert str(middle_node(ListNode.build([1, 2, 3, 4, 5, 6]))) == str(
        ListNode.build([4, 5, 6]))
