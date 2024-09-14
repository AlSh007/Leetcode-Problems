class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #the important property here is that the AND between two numbers is always smaller than the smaller number
        
        max_val = ans = cur_streak = 0
        
        for num in nums:
            if max_val < num:
                max_val = num
                ans = cur_streak = 0
                
            if max_val == num: #we encountered a bigger number so we will include it
                cur_streak += 1 
            
            else:
                cur_streak = 0
            
            ans = max(ans, cur_streak)
        
        return ans