class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_of_ones = s.count('1')
        
        n = len(s)
        
        return '1'*(count_of_ones - 1) + '0' * (n - count_of_ones) + '1'