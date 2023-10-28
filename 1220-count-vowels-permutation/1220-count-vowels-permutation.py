MOD = 10**9 + 7

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1]*5 #number of strings that end at i, with i = [a,e,i,o,u]
        
        for _ in range(2, n + 1):
            a, e, i, o, u = dp #for the i - 1 th number how many strings ended at given character
            
            dp[0] = (e + i + u) % MOD
            dp[1] = (a + i) % MOD 
            dp[2] = (e + o) % MOD
            dp[3] = i % MOD
            dp[4] = (i + o) % MOD
        
        #in the end dp will store the last state and we need permutations so we will add dp to get the number of strings ending at all characters
        return sum(dp) % MOD