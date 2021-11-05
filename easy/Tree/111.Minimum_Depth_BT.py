# solved with DFS
# class Solution:
#     def recurseDFS(self, node, level):
#         if node is not None:
#             right,left = level, level
#             if node.left:
#                 left = self.recurseDFS(node.left, level+1)
#             if node.right:
#                 right = self.recurseDFS(node.right, level+1)
                
#             if node.left and node.right is None:
#                 return left
#             elif node.right and node.left is None:
#                 return right
#             else:
#                 return min(left,right)
        
#     def minDepth(self, root):
#         node = root
#         if node:
#             return self.recurseDFS(node, 1)
#         else:
#             return 0

class Solution:
    #return the number of nodes of shortest path
    def minDepth(self, root):
        # ********** Using BFS **************  
        if not root:
            return 0
        # set an empty queue to trace the nodes already traversed
        from colllections import deque
        q = deque()

        # add root node into the queue
        q.append(root)

        # set a flag to specify whether we already have reached a leaf node (0 = No, 1 = yes)
        flag = 0

        depth = 0

        while len(q) > 0 and flag == 0:
            depth += 1 # executes at least once since "root" is on the queue

            for _ in range(len(q)):
                current_node = q.popleft()

                # check whether there is any children of the current_node and if not, set flag = 1
                if not current_node.left and not current_node.right:
                    flag = 1 # we reached a leaf node and we found our desired minDepth
                    break

                # add the children of current_node into the queue
                if current_node.left:
                    q.append(current_node.left)
                
                if current_node.right:
                    q.append(current_node.right)

        return depth

