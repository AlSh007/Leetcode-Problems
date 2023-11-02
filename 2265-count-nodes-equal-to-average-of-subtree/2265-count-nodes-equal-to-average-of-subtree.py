# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(node):
            nonlocal  ans
            if not node:
                return 0, 0
           
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            summ = left_sum + node.val + right_sum
            count = left_count + right_count + 1
            
            if summ//count == node.val:
                ans += 1
            
            return summ, count
        
        traverse(root)
        return ans