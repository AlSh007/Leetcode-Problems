# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: Optional[TreeNode]) -> str:
        if t is None:
            return ''
        result = str(t.val)
        if t.left:
            result += '(' + self.tree2str(t.left) + ')'
            if t.right:
                result += '(' + self.tree2str(t.right) + ')'
        elif t.right:
                result += '()' + '(' + self.tree2str(t.right) + ')'
        return result