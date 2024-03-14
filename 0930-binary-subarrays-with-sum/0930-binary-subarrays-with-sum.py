class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        curr_sum = 0
        
        freq = {}
        
        for num in nums:
            curr_sum += num
            
            if curr_sum == goal:
                total_count += 1
            
            if curr_sum - goal in freq:
                total_count += freq[curr_sum - goal]
            
            freq[curr_sum] = freq.get(curr_sum, 0) + 1
        
        return total_count