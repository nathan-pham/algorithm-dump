class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if self is other:
            return True

        if isinstance(other, TreeNode):
            def traverse(node_a, node_b):
                if node_a is None or node_b is None:
                    return node_a == node_b

                if node_a.val != node_b.val:
                    return False

                if node_a and node_b:
                    return (
                        traverse(node_a.left, node_b.left) and
                        traverse(node_a.right, node_b.right)
                    )

            if traverse(self, other) == False:
                return False

            return True

        return False


def merge_binary_tree(root_a, root_b):
    if root_a is None:
        return root_b
    if root_b is None:
        return root_a

    root_a.val += root_b.val
    root_a.left = merge_binary_tree(root_a.left, root_b.left)
    root_a.right = merge_binary_tree(root_a.right, root_b.right)
    return root_a


if __name__ == "__main__":
    assert merge_binary_tree(
        TreeNode(
            1,
            TreeNode(3, TreeNode(5), None),
            TreeNode(2, None, None)
        ),
        TreeNode(
            2,
            TreeNode(1, None, TreeNode(4)),
            TreeNode(3, None, TreeNode(7))
        )
    ) == TreeNode(
        3,
        TreeNode(4, TreeNode(5), TreeNode(4)),
        TreeNode(5, None, TreeNode(7))
    )

    assert merge_binary_tree(
        TreeNode(1),
        TreeNode(1, TreeNode(2), None)
    ) == TreeNode(
        2,
        TreeNode(2)
    )
