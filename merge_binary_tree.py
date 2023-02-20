class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build(values):
        tabs = [None] * len(values)

        for i in range(len(values)):
            parent_i = int((i - 1) / 2)
            parent = tabs[parent_i]
            new_node = TreeNode(values[i])
            if parent is not None:
                if parent.left is None:
                    parent.left = new_node
                elif parent.right is None:
                    parent.right = new_node

            tabs[i] = new_node

        return tabs[0]

    def toJSON(self):
        import json
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def toList(self):
        values = []
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            if isinstance(node, TreeNode):
                values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return values

    def __eq__(self, other):
        if other is self:
            return True

        if isinstance(other, TreeNode):
            return self.toList() == other.toList()

        return False

    def __str__(self):
        values = [str(v) for v in self.toList()]
        return f"[{', '.join(values)}]"


def merge_binary_tree(root_a, root_b):
    root_a_list = root_a.toList()
    root_b_list = root_b.toList()
    merged = [None] * max(len(root_a_list), len(root_b_list))
    for i in range(len(merged)):
        node_a = None
        try:
            node_a = root_a_list[i]
        except IndexError:
            pass

        node_b = None
        try:
            node_b = root_b_list[i]
        except IndexError:
            pass

        if node_a is None or node_b is None:
            if node_a is None:
                merged[i] = node_b
            elif node_b is None:
                merged[i] = node_a
        else:
            merged[i] = node_a + node_b

    return TreeNode.build(merged)


if __name__ == "__main__":
    assert merge_binary_tree(
        TreeNode.build([1, 3, 2, 5]),
        TreeNode.build([2, 1, 3, None, 4, None, 7])
    ) == TreeNode.build([3, 4, 5, 5, 4, None, 7])

    assert merge_binary_tree(
        TreeNode.build([1]),
        TreeNode.build([1, 2]),
    ) == TreeNode.build([2, 2])
