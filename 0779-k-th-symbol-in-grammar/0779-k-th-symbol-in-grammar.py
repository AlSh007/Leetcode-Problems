class Solution:
    def dfs(self, n, k, rootVal):
        if n == 1:
            return rootVal
        total_nodes = 2**(n - 1)
        if k > (total_nodes / 2):
            nextRootVal = 1 if rootVal == 0 else 0
            return self.dfs(n - 1, k - (total_nodes / 2), nextRootVal)
        else:
            nextRootVal = 0 if rootVal == 0 else 1
            return self.dfs(n - 1, k, nextRootVal)
    def kthGrammar(self, n: int, k: int) -> int:
        return self.dfs(n, k, 0)