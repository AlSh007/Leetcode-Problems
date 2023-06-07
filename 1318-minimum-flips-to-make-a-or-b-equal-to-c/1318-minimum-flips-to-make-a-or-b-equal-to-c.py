class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while(a or b or c):
            bit_a, bit_b, bit_c = a&1, b&1, c&1
            if(bit_a | bit_b != bit_c):
                if( bit_a == 1 and bit_b == 1):
                    count += 2
                else:
                    count += 1
            a = a>>1
            b = b>>1
            c = c>>1
        return count