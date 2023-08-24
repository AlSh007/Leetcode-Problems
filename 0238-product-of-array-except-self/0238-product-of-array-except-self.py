class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        pre, suf, n = list(accumulate(nums,mul)), list(accumulate(nums[::-1],mul))[::-1], len(nums)  
        return [(pre[i-1] if i else 1)*(suf[i+1] if i < n - 1 else 1) for i in range(n)]