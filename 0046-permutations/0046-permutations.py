class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur):
            if len(nums) == len(cur):
                ans.append(cur[:]) 
                return
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
        ans = []
        backtrack([])
        return ans