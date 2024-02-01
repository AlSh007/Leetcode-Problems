class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []

        for index in range(1, len(nums), 3):
            previous, current, next = nums[index - 1], nums[index], nums[index + 1]

            if next - previous > k:
                return []
            else:
                result.append([previous, current, next])

        return result