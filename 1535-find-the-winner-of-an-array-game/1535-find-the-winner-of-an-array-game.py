class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        winstreak = 0
        cur = arr[0]
        
        for i in range(1, n):
            if arr[i] < cur:
                winstreak += 1
            else:
                if winstreak >= k:
                    return cur
                cur = arr[i]
                winstreak = 1
        
        return cur