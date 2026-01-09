# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deepest_depth(node, depth):
            if not node:
                return node, depth
            
            left, leftDepth = deepest_depth(node.left, depth + 1)
            right, rightDepth = deepest_depth(node.right, depth + 1)

            if leftDepth > rightDepth: