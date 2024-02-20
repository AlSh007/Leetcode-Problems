class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for count, value in enumerate(nums):
            ans ^= count + 1
            ans ^= value
        
        return ans