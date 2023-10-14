class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        # Base case: If we have zero walls to paint, the cost is zero.
        for i in range(n + 1):
            dp[i][0] = 0

        for ind in range(n):
            for walls in range(1, n + 1):
                take = cost[ind]  # Initialize take as the cost of the current wall
                remaining_walls = walls - time[ind] - 1

                if remaining_walls >= 0:
                    take += dp[ind][remaining_walls]

                not_take = dp[ind][walls]

                dp[ind + 1][walls] = min(take, not_take)

        return dp[n][n]