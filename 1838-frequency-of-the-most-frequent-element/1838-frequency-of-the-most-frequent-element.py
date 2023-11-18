class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            target = nums[right]
            curr_sum += target
            
            while (right - left + 1)*target - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans