class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = defaultdict(int)
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
        ans = []
        for num, freq in dic.items():
            if freq > n//3:
                ans.append(num)
        
        return ans