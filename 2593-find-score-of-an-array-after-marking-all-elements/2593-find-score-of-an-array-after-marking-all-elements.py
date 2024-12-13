class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums.append(float("inf"))
        res = 0
        start = -1
        i = 1
        while i < len(nums):
            if nums[i] >= nums[i - 1]:
                for j in range(i - 1, start, -2):
                    res += nums[j]
                start = i
                i += 1
            i += 1
        return res