class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        ans = 0
        i = 0
        for j in range(len(s)):
            # print("h")
            while s[j] in ss:
                ss.remove(s[i])
                i+=1
            ans = max(ans, j -i + 1)
            ss.add(s[j])
            j += 1

        return ans

            
        