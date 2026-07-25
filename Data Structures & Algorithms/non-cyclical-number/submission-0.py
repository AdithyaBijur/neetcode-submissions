class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1 and n not in seen:
            digits = []
            seen.add(n)
            while n:
                digits.append(n%10)
                n = n // 10
            
            square = 0
            for i in digits:
                square = math.pow(i, 2) + square
            
            n = square
        
        return n == 1