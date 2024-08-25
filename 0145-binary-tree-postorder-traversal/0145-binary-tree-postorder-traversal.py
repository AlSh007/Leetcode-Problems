# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _postorder_traversal(self, curr_node, result):
        if not curr_node:
            return
        self._postorder_traversal(curr_node.left, result)
        self._postorder_traversal(curr_node.right, result)
        
        result.append(curr_node.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        self._postorder_traversal(root, result)
        
        return result