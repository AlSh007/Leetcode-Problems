class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                l, r = j + 1, n - 1
                remainingVal = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remainingVal:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > remainingVal:
                        r -= 1
                    else:
                        l += 1
        
        return ans