class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        increase = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                increase += 1
            
            ans += increase
        
        return ans