class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        count = 1
        seats = 0
        
        prev_pair_last = None
        
        for index, thing in enumerate(corridor):
            if thing == 'S':
                seats += 1
                
                if seats == 2:
                    prev_pair_last = index
                    seats = 0
                
                if seats == 1 and prev_pair_last is not None:
                    count *= (index - prev_pair_last)
                    count %= MOD
        if seats == 1 or prev_pair_last is None:
            return 0
        
        return count