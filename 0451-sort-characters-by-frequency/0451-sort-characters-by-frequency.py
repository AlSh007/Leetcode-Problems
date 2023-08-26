class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for char, freq in cnt.items():
            bucket[freq].append(char)
        ans = []
        for freq in range(n,-1,-1):
            for char in bucket[freq]:
                ans.append(char*freq)
        return ''.join(ans)
        