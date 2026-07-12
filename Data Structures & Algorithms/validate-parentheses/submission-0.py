class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ']' : '[',
            '}' : '{',
            ')' : '(',
        }

        stack = []

        for i in s:
            if i not in close:
                stack.append(i)
            else:
                if not stack or close[i] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) > 0:
            return False
        return True
        