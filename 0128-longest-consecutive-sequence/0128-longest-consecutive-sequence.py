class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        cur = min(1,len(nums))
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] +1 == nums[i]:
                cur += 1
                ans = max(ans,cur)
            else:
                cur = 1
        return max(ans,cur)
            