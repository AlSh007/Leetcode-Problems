class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        LUT = SparseTable(nums)

        pq = [(-LUT.query(i, n), i, n) for i in range(n)]

        res = 0
        for _ in range(k):
            val, l, r = pq[0]
            if val == 0:
                break
            res -= val
            heapq.heapreplace(pq, (-LUT.query(l, r - 1), l, r - 1))

        return res

class SparseTable:
    def __init__(self, num: list[int]):
        n = len(num)
        bitWidth = n.bit_length()
        self.Min = [[0] * n for _ in range(bitWidth)]
        self.Max = [[0] * n for _ in range(bitWidth)]

        for i in range(n):
            self.Min[0][i] = self.Max[0][i] = num[i]