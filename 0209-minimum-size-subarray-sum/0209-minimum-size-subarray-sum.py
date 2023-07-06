class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        ans, n, arrSum = float('inf'), len(nums), 0 
        while right < n:
            arrSum += nums[right]
            right += 1
            while arrSum >= target:
                ans = min(ans,right-left)
                arrSum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans