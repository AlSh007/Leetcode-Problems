class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        for num, freq in count.items():
            if freq > n // 4:
                return num
        
        return 0