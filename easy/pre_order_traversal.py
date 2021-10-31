class Solution:
    def preorderTraversal(self, root):
        result = []

        def traverse(root):
            if root is None:
                return

            result.append(root.val)

            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)
                
        traverse(root)
        return result
