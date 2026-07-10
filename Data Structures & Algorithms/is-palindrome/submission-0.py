class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1

        def isNotValid(s):
            if (s >= 'A' and s <='Z') or (s >= 'a' and s <= 'z') or (s >= '0' and s <= '9'):
                return False
            return True

        while i < j:
            print(s[i], s[j])
            if isNotValid(s[i]):
                i += 1
                continue
            if isNotValid(s[j]):
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        
        return True