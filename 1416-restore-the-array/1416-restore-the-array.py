class Solution:
    def dfs(self,s,k,i,dp):
        if i==len(s):
            return 1
        if s[i]=='0':
            return 0
        if dp[i]!=-1:
            return dp[i]
        num=0
        ans=0
        for j in range(i,len(s)):
            num=num*10+int(s[j])
            if num>k:
                break
            ans=(ans+self.dfs(s,k,1+j,dp))%1000000007
        dp[i]=ans
        return ans
            
    def numberOfArrays(self, s: str, k: int) -> int:
        dp=[-1]*len(s)
        return self.dfs(s,k,0,dp)