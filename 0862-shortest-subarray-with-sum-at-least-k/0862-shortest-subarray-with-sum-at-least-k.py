class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        Q = deque([[0,0]])
        
        res, cur_sum = float('inf'), 0
        
        for ind, num in enumerate(nums):
            cur_sum += num
            
            while Q and cur_sum - Q[0][1] >= k:
                res = min(res, ind + 1 - Q[0][0])
                Q.popleft()
            
            while Q and cur_sum <= Q[-1][1]:
                Q.pop()
            
            Q.append([ind + 1, cur_sum])
        
        return res if res < float('inf') else -1