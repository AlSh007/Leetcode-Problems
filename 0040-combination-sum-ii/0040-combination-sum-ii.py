class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def solve(curr_sum , i , curr_comb):
            if curr_sum == target:
                ans.append(curr_comb[:])
                return
            if curr_sum > target:
                return
            for ind in range(i , n):
                if ind > i and candidates[ind] == candidates[ind-1]:
                    continue
                curr_comb.append(candidates[ind])
                solve(curr_sum + candidates[ind], ind + 1, curr_comb)
                curr_comb.pop()
        
        solve(0, 0, [])
        return ans
                