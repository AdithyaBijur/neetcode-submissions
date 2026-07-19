class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s)):
            #odd
            j = i
            k = i
            while  j >= 0 and k < len(s) and s[j] == s[k]: #condition ordering is importat
                ans += 1
                j -= 1
                k += 1
            
            #even
            j = i
            k = i+ 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                ans += 1
                j -= 1
                k += 1
        return ans