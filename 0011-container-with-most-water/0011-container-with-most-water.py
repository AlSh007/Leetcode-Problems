class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, left, right, maxWater = 0, 0, len(height) - 1, 0
        
        while left < right:
            if height[left] <= height[right]:
                ans = height[left]*(right - left)
                left += 1
            else:
                ans = height[right]*(right - left)
                right -= 1
            
            maxWater = max(ans, maxWater)
            
        return maxWater