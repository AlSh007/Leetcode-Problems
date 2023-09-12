class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        seen_frequencies = set()
        deletions = 0
        
        for char, freq in count.items():
            while freq > 0 and freq in seen_frequencies:
                freq -= 1
                deletions += 1
            seen_frequencies.add(freq)
        
        return deletions