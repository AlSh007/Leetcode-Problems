class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count = defaultdict(int)
        
        count[0] = 1
        
        for num in nums:
            step = defaultdict(int)
            
            for y in count:
                step[y + num] += count[y]
                step[y - num] += count[y]
            
            count = step
        
        return count[target]