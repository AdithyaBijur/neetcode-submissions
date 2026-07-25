class Solution:
    def reverseBits(self, n: int) -> int:

        rev = 0
        for i in range(0, 32):
            bit = (1 << i) & n
            if bit > 0:
                rev = rev | (1<<(31-i))
        
        return rev
        