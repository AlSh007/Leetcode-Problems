class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        occurences = set()
        
        for value, occurence in count.items():
            if occurence not in occurences:
                occurences.add(occurence)
            else:
                return False
        
        return True