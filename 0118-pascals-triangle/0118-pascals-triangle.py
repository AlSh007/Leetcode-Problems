class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1,n+1)]
        for i in range(1,n):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans