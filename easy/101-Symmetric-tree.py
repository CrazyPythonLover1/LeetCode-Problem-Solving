class Solution:
    def isSymmetric(self, root):
        def isSym(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None: 
                return False
            if p.val != q.val:
                return False
            return isSym(p.left, q.right) and isSym(p.right, q.left)
        return isSym(root.left, root.right)
