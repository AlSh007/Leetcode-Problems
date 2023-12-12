class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        largest = nums[-1]
        second_lgt = nums[-2]
        
        return (largest - 1)*(second_lgt - 1)