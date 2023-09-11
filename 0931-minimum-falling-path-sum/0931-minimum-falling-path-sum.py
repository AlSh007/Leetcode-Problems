class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[float('inf')]*n for _ in range(m)]
        def dfs(i, j):
            if i==m-1 and j >= 0 and j < n:
                return matrix[i][j]
            if j >= n or j<0:
                return float('inf')
            if dp[i][j] != float('inf'):
                return dp[i][j]
            
            down =  dfs(i+1,j)
            lower_left =  dfs(i+1,j-1)
            lower_right =  dfs(i+1,j+1)
            ans = matrix[i][j] + min(down,lower_left,lower_right)
            dp[i][j] = ans
            return ans
        
        final_ans = float('inf')
        for i in range(n):
            final_ans = min(final_ans,dfs(0,i))
        return final_ans
        