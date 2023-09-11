class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                upper_left = matrix[i-1][j-1] if j-1 >= 0 else float('inf')
                up = matrix[i-1][j]
                upper_right = matrix[i-1][j+1] if j + 1 < n else float('inf')
                matrix[i][j] += min(upper_left, up, upper_right)
        return min(matrix[n-1])
        