class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = cur_penalty = 0
        earliest_hour = 0
        for ind, char in enumerate(customers):
            if char == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            
            if min_penalty > cur_penalty:
                earliest_hour = ind + 1
                min_penalty = cur_penalty
            
                
        return earliest_hour
        
        