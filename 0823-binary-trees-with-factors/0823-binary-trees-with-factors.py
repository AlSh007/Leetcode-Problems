class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        arr.sort()
        MOD = 10**9 + 7
        
        for num in arr:
            dp[num] = 1
        
        for i, num in enumerate(arr):
            for j in range(i): #we are running for loop until we reach our current number so we will check if our number has any factors, since its a sorted array factors will be on the left side of the number
                if num%arr[j] == 0 and num // arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]]
                    dp[num] %= MOD
        
        return sum(dp.values()) % MOD