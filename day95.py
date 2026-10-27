class Solution:
    def generateTrees(self, n):
        def build(start, end):
            if start > end:
                return [None]

            result = []

            for root in range(start, end + 1):
                leftTrees = build(start, root - 1)
                rightTrees = build(root + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        result.append(node)

            return result

        return build(1, n)