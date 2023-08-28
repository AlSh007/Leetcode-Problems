class Solution:
    def dfs(self,nums,cur,ans):
        ans.append(cur)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], cur + [nums[i]],ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums,[],ans)
        return ans