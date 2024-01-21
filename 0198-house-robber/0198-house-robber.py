class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev, cur = 0, 0, 0
        for i in nums:
            cur = max(prev,i + prev2)
            prev2 = prev
            prev = cur
        return cur
            