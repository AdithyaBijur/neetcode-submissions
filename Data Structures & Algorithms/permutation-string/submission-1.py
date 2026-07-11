class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        def same(d1,d2):
            return d1 == d2


        s1C = collections.defaultdict(int)
        for i in s1:
            s1C[i] += 1
        
        s2C = collections.defaultdict(int)

        for i in range(0, len(s1)):
            s2C[s2[i]] += 1
        
        if same(s1C, s2C):
            return True
        i = 0
        for j in range(len(s1), len(s2)):
            s2C[s2[i]] -= 1
            if s2C[s2[i]] == 0:
                del(s2C[s2[i]])
            i+=1
            s2C[s2[j]] += 1
            if same(s1C, s2C):
                return True
            
        return False
                   