class Solution:
        

    def smallestIndex(self, nums: List[int]) -> int:
        for ind, num in enumerate(nums):

            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10


            if ind == sum:
                return ind
        
        return -1