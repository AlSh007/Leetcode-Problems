class Solution:
    def reorganizeString(self, s: str) -> str:
        res, c = [], Counter(s)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        char_freq, char = 0, ''
        
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if char_freq < 0:
                heapq.heappush(pq,(char_freq, char))
            a += 1
            char_freq, char = a, b
        res = ''.join(res)
        if len(res) != len(s):
            return ''
        return res