class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        k -= 1
        min_diff = float('inf')
        for i in range(len(nums) - k):
            min_diff = min(min_diff, nums[i+k] - nums[i])
        
        return min_diff