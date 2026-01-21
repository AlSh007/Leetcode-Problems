class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num % 2 == 0:
                res.append(-1)
            else:
                res.append(num - ((num + 1) & (-num - 1)) // 2)
        
        return res