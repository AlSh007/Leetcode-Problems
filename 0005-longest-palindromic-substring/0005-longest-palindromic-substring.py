class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, max_pal_len = 0, 1
        
        for i in range(n):
            right = i
            
            while right < n and s[right] == s[i]:
                right += 1
            
            left = i - 1
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            pal_len = right - left - 1
            if pal_len > max_pal_len:
                start = left + 1
                max_pal_len = pal_len
            
        return s[start:start + max_pal_len]
            
            