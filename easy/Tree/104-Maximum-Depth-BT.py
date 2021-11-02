class Solution:
    def maxDepth(self, root):
        number_of_left_nodes = 1
        number_of_right_nodes = 1
        
        if root is None:
            return 0
        
        leftNode = root.left
        
        while leftNode:
            number_of_left_nodes += 1
            leftNode = leftNode.left
        
        rightNode = root.right
        
        while rightNode:
            number_of_right_nodes += 1
            rightNode = rightNode.right

        if number_of_left_nodes > number_of_right_nodes:
            return number_of_left_nodes
        elif number_of_right_nodes > number_of_left_nodes:
            return number_of_right_nodes
        elif number_of_left_nodes > 1 and number_of_left_nodes == number_of_right_nodes:
            return number_of_left_nodes
        elif root.left is None and root.right is None:
            return 1
        