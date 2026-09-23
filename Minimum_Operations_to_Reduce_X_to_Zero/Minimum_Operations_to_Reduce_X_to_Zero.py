class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        left, cur_sum, max_len = 0, 0, 0
        n = len(nums)

        if target == 0:
            return n
        
        for right, val in enumerate(nums):
            cur_sum += val

            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
            
        
        return n - max_len if max_len > 0 else -1