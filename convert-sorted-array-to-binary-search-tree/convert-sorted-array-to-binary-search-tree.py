# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(0,nums,len(nums))
    
    def makeBST(self,start,nums,end):
        if start>=end:
            return None
        mid = (start+end)//2
        return TreeNode(
            val = nums[mid],
            left = self.makeBST(start,nums,mid),
            right = self.makeBST(mid+1,nums,end)
        )
        