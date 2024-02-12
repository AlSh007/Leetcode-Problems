class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        
        for elem ,freq in count.items():
            if freq > n // 2:
                return elem
        
        return -1