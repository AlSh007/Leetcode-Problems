class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        k = max(count.values()) 
        print(k)
        num = list(count.elements())
        print(num)
        
        return [num[i::k] for i in range(k)]