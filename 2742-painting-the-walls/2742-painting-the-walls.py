class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(ind, walls):
            if walls <= 0:
                return 0
            if ind < 0:
                return inf
            if dp[ind][walls] != -1:
                return dp[ind][walls]
            take = cost[ind] + solve(ind - 1, walls - time[ind] - 1)
            not_take = 0 + solve(ind - 1, walls)
            dp[ind][walls] = min(take, not_take)
            return dp[ind][walls]
        
        return solve(n-1, n)