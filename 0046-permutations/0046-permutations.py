class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()

        backtrack([])
        return ans