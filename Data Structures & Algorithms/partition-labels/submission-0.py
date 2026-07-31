class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIndex = collections.defaultdict(int)
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        boundary = 0
        past = -1
        ans = []

        i = 0

        while i < len(s):
            boundary = max(boundary, lastIndex[s[i]])
            if i == boundary:
                ans.append(i - past)
                past = i
            i+=1
        
        return ans

            