class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        
        j = -1
        
        prevMinIndex = -1
        prevMaxIndex = -1
        
        for i, num in enumerate(nums):
            if minK > num or num > maxK:
                j = i
            
            if num == minK:
                prevMinIndex = i
            
            if num == maxK:
                prevMaxIndex = i
            
            ans += max(0, min(prevMinIndex, prevMaxIndex) - j)
        
        return ans
        
        