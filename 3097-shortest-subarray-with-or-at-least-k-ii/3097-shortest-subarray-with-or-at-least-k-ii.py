class Solution:
    def update(self, bits, x, change):
        for i in range(32):
            if (x>>i) & 1:
                bits[i] += change
    
    def bits_to_num(self, bits):
        result = 0
        for i in range(32):
            if bits[i]:
                result |= (1 << i)
        
        return result
        
    
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = n + 1
        bits = [0] * 32
        start = 0
        
        for end in range(n):
            self.update(bits, nums[end], 1)
            while start <= end and self.bits_to_num(bits) >= k:
                result = min(result, end - start + 1 )
                self.update(bits, nums[start], -1)
                start += 1
        
        return result if result != n + 1 else -1