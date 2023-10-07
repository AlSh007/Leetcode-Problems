# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root == None:
                return 0
            return 1 + max(height(root.left),height(root.right))
        
        if root == None:
            return True
        left_ht = height(root.left)
        right_ht = height(root.right)
        if abs(left_ht - right_ht) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        