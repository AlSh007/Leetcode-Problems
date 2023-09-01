class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            temp = i
            count = 0
            while temp:
                temp = temp&(temp-1)
                count += 1
            ans[i] = count
        return ans