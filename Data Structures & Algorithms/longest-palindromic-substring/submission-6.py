from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        ansS = 0
        for i in range(0, len(s)):
            #odd
            j = i
            k = i
            while  j >= 0 and k < len(s) and s[j] == s[k]: #condition ordering is importat
                ans = max(ans, k - j + 1)
                if ans ==  k - j + 1:
                    ansS = j
                j -= 1
                k += 1
            
            #even
            j = i
            k = i+ 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                ans = max(ans, k - j + 1)
                if ans ==  k - j + 1:
                    ansS = j
                j -= 1
                k += 1
        print(ans)
        return s[ansS: ansS + ans]