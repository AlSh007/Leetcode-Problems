# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        return self._check_path(root, head)
    
    def _check_path(self, node, head):
        if node is None:
            return False
        if self.dfs(node, head):
            return True
        
        return self._check_path(node.left, head) or self._check_path(node.right, head)
    
    def dfs(self, node, head):
        if head is None:
            return True
        
        if node is None:
            return False
        
        if node.val != head.val:
            return False
        
        return self.dfs(node.left, head.next) or self.dfs(node.right, head.next)