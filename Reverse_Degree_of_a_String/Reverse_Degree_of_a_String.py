class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, idx = 0, 1

        for char in s:
            ans += (123 - ord(char)) * idx
            idx += 1
        
        return ans