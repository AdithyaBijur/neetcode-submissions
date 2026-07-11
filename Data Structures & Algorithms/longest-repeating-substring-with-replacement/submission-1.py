class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i = 0
        seen = collections.defaultdict(int)
        ans = 0
        for j in range(len(s)):
            seen[s[j]] += 1
            maxx = max(seen.values())
            while (j-i +1) - maxx > k:
                seen[s[i]] -= 1
                i += 1
            ans = max(ans, j-i + 1)
        
        return ans
            

        
            