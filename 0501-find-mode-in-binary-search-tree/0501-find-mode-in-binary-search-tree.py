# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            dic[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        ans = []
        mode = max(dic.values())
        for key in dic:
            if dic[key] == mode:
                ans.append(key)
        return ans