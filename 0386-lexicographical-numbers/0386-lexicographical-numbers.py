class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        current_number = 1
        
        for i in range(n):
            res.append(current_number)
            
            if current_number * 10 <= n:
                current_number *= 10
            
            else:
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10
                
                current_number += 1
            
        return res