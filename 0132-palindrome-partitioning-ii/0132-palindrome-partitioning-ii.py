class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1]*n
        if s == s[::-1]: return 0
        
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        def isPalindrome(i , j):
            while i < j:
                if s[i] != s[j]:
                    return False 
                i += 1
                j -= 1
            
            return True
                

        def solve(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            min_cost = float('inf')
            
            for j in range(i,n):
                if isPalindrome(i, j):
                    cost  = 1 + solve(j + 1)
                    min_cost = min(min_cost, cost)
            dp[i] = min_cost
            return dp[i]
        
        return solve(0) - 1