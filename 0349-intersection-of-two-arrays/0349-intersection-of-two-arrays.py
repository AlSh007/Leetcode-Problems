class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        ans = []
        seen = defaultdict(bool)
        
        for num in nums2:
            seen[num] = True
        
        for num in nums1:
            if seen[num]:
                ans.append(num)
                seen[num] = False
        
        return ans