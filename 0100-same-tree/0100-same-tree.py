# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check_tree(p, q):
            if p == None and q == None:
                return True
            
            if p is None or q is None:
                return False
            if p.val == q.val and check_tree(p.left, q.left) and check_tree(p.right, q.right):
                return True
            return False
        
        return check_tree(p, q)