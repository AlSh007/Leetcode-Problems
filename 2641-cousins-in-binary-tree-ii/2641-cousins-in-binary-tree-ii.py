# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level_sums = [0] * 100000
        
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.calculate_level_sum(root, 0)
        self.replace_value_in_tree_helper(root, 0, 0)
        return root
    
    def calculate_level_sum(self, node, level):
        if node is None:
            return 
        self.level_sums[level] += node.val
        self.calculate_level_sum(node.left, level + 1)
        self.calculate_level_sum(node.right, level + 1)
    
    def replace_value_in_tree_helper(self, node, sibling_sum, level):
        if node is None:
            return
        left_child_val = 0 if node.left is None else node.left.val
        right_child_val = 0 if node.right is None else node.right.val
        
        if level == 0 or level == 1:
            node.val = 0
        
        else:
            node.val = self.level_sums[level] - node.val - sibling_sum
        
        self.replace_value_in_tree_helper(node.left, right_child_val, level + 1)
        self.replace_value_in_tree_helper(node.right, left_child_val, level + 1)