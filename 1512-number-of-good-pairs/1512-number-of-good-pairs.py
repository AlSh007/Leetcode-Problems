class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        good_pairs = 0
        print(c)
        for num, freq in c.items():
            if freq > 1:
                good_pairs += (freq-1)*(freq)//2
        
        return good_pairs