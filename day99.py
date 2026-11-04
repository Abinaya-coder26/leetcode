
class Solution:
    def recoverTree(self, root):
        nodes = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        first = None
        second = None

        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if first is None:
                    first = nodes[i]

                second = nodes[i + 1]

        first.val, second.val = second.val, first.val
