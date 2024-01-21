class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        one_cnt = 0
        two_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
            elif i == 1:
                one_cnt += 1
            elif i == 2:
                two_cnt += 1
        for i in range(len(nums)):
            if zero_cnt != 0:
                nums[i] = 0
                zero_cnt -= 1
            elif one_cnt != 0:
                nums[i] = 1
                one_cnt -= 1
            else:
                nums[i] = 2
                two_cnt -= 1
        