class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        unique_sum = sum(set(nums))
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        duplicate, missing = actual_sum - unique_sum, expected_sum - unique_sum
        return [duplicate, missing]