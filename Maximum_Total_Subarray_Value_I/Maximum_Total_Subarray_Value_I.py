class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        global_max = global_min = nums[0]

        for num in nums:
            global_min = min(global_min, num)
            global_max = max(global_max, num)
        
        return (global_max - global_min) * k