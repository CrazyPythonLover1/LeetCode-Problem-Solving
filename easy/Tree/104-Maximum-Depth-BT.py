


# class Solution:
#     def maxDepth(self, root):
#         number_of_left_nodes = 1
#         number_of_right_nodes = 1
        
#         if root is None:
#             return 0
        
#         leftNode = root.left
        
#         while leftNode:
#             number_of_left_nodes += 1
#             leftNode = leftNode.left
        
#         rightNode = root.right
        
#         while rightNode:
#             number_of_right_nodes += 1
#             rightNode = rightNode.right

#         if number_of_left_nodes > number_of_right_nodes:
#             return number_of_left_nodes
#         elif number_of_right_nodes > number_of_left_nodes:
#             return number_of_right_nodes
#         elif number_of_left_nodes > 1 and number_of_left_nodes == number_of_right_nodes:
#             return number_of_left_nodes
#         elif root.left is None and root.right is None:
#             return 1
        
class Solution:
    
    def recurseDFS(self, node, level):
        if node is not None:
            right,left = level, level
            if node.left is not None:
                left = self.recurseDFS(node.left, level+1)
            if node.right is not None:
                right = self.recurseDFS(node.right, level+1)
            return max(left, right)
                        

    def maxDepth(self, root):
        node = root
        if node is not None:
            return self.recurseDFS(node, 1)
        else:
            return 0
