class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        s = list(s)
        s.sort(key = lambda x:(-cnt[x],x))
        return ''.join(s)
        