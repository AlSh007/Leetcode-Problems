class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = -inf
        for num in nums[::-1]:
            if num < s3: #one number is smaller than s3 thus we have the triplet because s3 will be a valid number from the last stack op
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False