class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                ans += prev * cnt
                prev = cnt
        
        return ans