class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            matching_pair = target - nums[i]
            if matching_pair in hashmap:
                return [i, hashmap[matching_pair]]
            hashmap[nums[i]] = i