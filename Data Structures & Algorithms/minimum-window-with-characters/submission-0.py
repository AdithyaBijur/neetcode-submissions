class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = collections.defaultdict(int)

        for i in t:
            td[i] += 1
        
        def isValid(d1, d2):
            for key in d2:
                if d1[key] < d2[key]:
                    return False
                
            return True
        
        sd = collections.defaultdict(int)
        i = 0
        ans = float("inf")
        anss = ""
        for j in range(len(s)):
            sd[s[j]] += 1
            if not isValid(sd, td):
                continue
            while isValid(sd,td):
                ans = min(ans, j - i + 1)
                if ans == j -i +1:
                    anss = s[i:j+1]
                sd[s[i]] -=1
                i+=1
        return anss
            

