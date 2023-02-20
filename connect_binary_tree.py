from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(node: Optional[Node] = None) -> Optional[Node]:
    if node is None:
        return node

    if node.left is not None:
        node.left.next = node.right

    if node.right is not None:
        if node.next is not None:
            node.right.next = node.next.left
        # else:
        #     node.right.next = None

    connect(node.left)
    connect(node.right)

    return node


def print_json(obj):
    import json
    print(json.dumps(obj, default=lambda o: o.__dict__,
                     sort_keys=True, indent=4))


if __name__ == "__main__":
    print_json(connect(Node(
        1,
        Node(2, Node(4), Node(5)),
        Node(3, Node(6), Node(7))
    )))
    #     Input: root = [1,2,3,4,5,6,7]
    # Output: [1,#,2,3,#,4,5,6,7,#]
