# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            dic[root.val] += 1
            inorder(root.right)
        
        ans = []
        inorder(root)
        mode = max(dic.values())
        for key in dic:
            if dic[key] == mode:
                ans.append(key)
        return ans