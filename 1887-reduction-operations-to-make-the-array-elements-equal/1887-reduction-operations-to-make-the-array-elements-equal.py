class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        increase = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                increase += 1 #everytime we get a larger number we will have to do more operations, since the larger elements will be decreased to next larger first we will increament this variable to 
            
            ans += increase #we will add all the levels of increasing numbers to the final ans
        
        return ans