class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        montonic_inc = False
        monotonic_dec = False
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                montonic_inc = True
            elif nums[i] < nums[i-1]:
                monotonic_dec = True
        return not (montonic_inc & monotonic_dec)
        