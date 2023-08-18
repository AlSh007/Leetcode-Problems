class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        while x:
            num *= 10;
            num += x%10
            x //= 10
        if flag:
            num *= -1
        
        return num if -pow(2,31) <= num <= pow(2,31) else 0