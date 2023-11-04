class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 0
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
        
        for i in range(n-1, -1, -1):
            min_cost = float('inf')
            
            for j in range(i, n):
                if isPalindrome(i, j):
                    cost = 1 + dp[j+1]
                    min_cost = min(min_cost, cost)
            
            dp[i] = min_cost
                

        
        
        return dp[0] - 1