class Solution:
    def inorderTraversal(self, root):
        result = []
        def traverse(root):
            if root is None:
                return
            
            if root.left:
                traverse(root.left)
                
            result.append(root.val)
            
            if root.right:
                traverse(root.right)
                
        traverse(root)
        return result
