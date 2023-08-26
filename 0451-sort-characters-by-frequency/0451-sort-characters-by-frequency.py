class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        arr = [[freq,c] for c, freq in cnt.items()]
        arr.sort(key = lambda x:-x[0])
        ans = []
        for freq, char in arr:
            ans.append(freq*char)
        return ''.join(ans)
        