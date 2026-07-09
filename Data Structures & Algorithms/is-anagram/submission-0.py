class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = collections.defaultdict(int)
        s2 = collections.defaultdict(int)

        for i in s:
            s1[i] += 1
        
        for j in t:
            s2[j] += 1

        
        for i in s1:
            if s2[i] != s1[i]:
                return False

        for j in s2:
            if s1[j] != s2[j]:
                return False
        
        
        return True
