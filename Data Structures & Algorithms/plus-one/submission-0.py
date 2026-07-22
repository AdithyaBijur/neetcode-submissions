class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        

        carry = digits[-1] // 10
        digits[-1] =  digits[-1] % 10
        for i in range(len(digits) - 2, -1, -1):
            if carry == 0:
                return digits
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] =  digits[i] % 10
        if carry != 0:
            digits = [carry] + digits
        return digits