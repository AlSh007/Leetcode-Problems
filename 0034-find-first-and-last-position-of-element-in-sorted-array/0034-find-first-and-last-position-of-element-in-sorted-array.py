class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(num):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) //2
                if nums[mid] >= num:
                    high = mid
                else:
                    low = mid + 1
            return low
        low = search(target)
        return [low, search(target+1) - 1] if target in nums[low:low+1] else [-1,-1]