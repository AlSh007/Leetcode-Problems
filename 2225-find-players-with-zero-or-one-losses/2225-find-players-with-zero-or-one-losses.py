class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt_loser = defaultdict(int)
        
        for w, l in matches:
            cnt_loser.setdefault(w, 0)
            cnt_loser[l] += 1
            
        return [sorted(l for l, c in cnt_loser.items() if c == 0),
               sorted(l for l, c in cnt_loser.items() if c == 1)]