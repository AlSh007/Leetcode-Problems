class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, s = 0, set(nums)
        for num in nums:
            if num - 1 in s:
                continue
            j = 1
            while num + j in s:
                j += 1
            longest = max(longest, j)
        return longest