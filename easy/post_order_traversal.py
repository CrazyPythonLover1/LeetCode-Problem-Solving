class Solution:
    def postorderTraversal(self, root):
        result = []
        def traverse(root):
            if root is None:
                return

            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)

            result.append(root.val)
            
        traverse(root)
        return result
    
        