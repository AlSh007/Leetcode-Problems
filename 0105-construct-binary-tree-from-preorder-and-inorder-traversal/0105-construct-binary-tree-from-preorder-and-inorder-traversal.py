# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            val = preorder.pop(0)
            ind = inorder.index(val)

            root = TreeNode(inorder[ind])

            root.left = self.buildTree(preorder,inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])

            return root