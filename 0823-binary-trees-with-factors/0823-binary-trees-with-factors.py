class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        arr.sort()
        MOD = 10**9 + 7
        
        for num in arr:
            dp[num] = 1
        
        for i, num in enumerate(arr):
            for j in range(i): #we are running for loop for count because if we use any number as a root more than one time it will be the same tree
                if not(num%arr[j]) and num // arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]]
                    dp[num] %= MOD
        
        return sum(dp.values()) % MOD