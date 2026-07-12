class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        required = len(need)
        formed = 0
        
    
        window = collections.defaultdict(int)
        i = 0
        ans = float("inf")
        anss = ""
        for j in range(len(s)):
            window[s[j]] += 1
            if s[j] in need and need[s[j]] == window[s[j]]:
               formed += 1
            
            while formed == required:
                ans = min(ans, j - i + 1)
                if ans == j -i +1:
                    anss = s[i:j+1]
                window[s[i]] -=1
                if s[i] in need and need[s[i]] > window[s[i]]:
                    formed -= 1 
                i+=1
        return anss
            

