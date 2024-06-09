class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderFreq = defaultdict(int)
        
        remainderFreq[0] = 1
        
        res = prefixSum = 0
        
        for num in nums:
            
            prefixSum += num
            
            remainder = prefixSum % k
            
            res += remainderFreq[remainder]
            
            remainderFreq[remainder] += 1
        
        return res
        