class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(target_list, i, cur_sum):
            
            if cur_sum > target:
                return
            
            if(cur_sum == target):
                ans.append(target_list)
                return
            
            for j in range(i, n):
                dfs(target_list + [candidates[j]], j , cur_sum + candidates[j])
        
        
        dfs([], 0, 0)
        return ans