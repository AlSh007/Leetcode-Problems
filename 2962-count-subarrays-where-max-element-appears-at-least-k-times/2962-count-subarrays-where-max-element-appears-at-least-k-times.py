class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        cnt_max_elem = 0
        start, count = 0, 0
        
        for end in range(len(nums)):
            
            if nums[end] == max_elem:
                cnt_max_elem += 1
            
            while cnt_max_elem >= k:
                
                
                if nums[start] == max_elem:
                    cnt_max_elem -= 1
                
                start += 1
            count += start
        
        return count
                
                