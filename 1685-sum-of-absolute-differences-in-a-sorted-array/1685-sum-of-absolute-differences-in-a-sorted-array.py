class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        ans = []
        
        for i, num in enumerate(nums):
            right_sum -= num
            ans.append(right_sum - (n - 1 - i)*num + i*num - left_sum)
            left_sum += num
        
        return ans
        