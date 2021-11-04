# solved with DFS
class Solution:
    def recurseDFS(self, node, level):
        if node is not None:
            right,left = level, level
            if node.left:
                left = self.recurseDFS(node.left, level+1)
            if node.right:
                right = self.recurseDFS(node.right, level+1)
                
            if node.left and node.right is None:
                return left
            elif node.right and node.left is None:
                return right
            else:
                return min(left,right)
        
    def minDepth(self, root):
        node = root
        if node:
            return self.recurseDFS(node, 1)
        else:
            return 0
        