class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        i = 0
        j = 0
        ans = []
        while j < len(s):
            while s[j] != '#':
                j +=1
            l = int(s[i:j])
            ans.append(s[j+1:j + l + 1])
            i = j + l + 1
            j = i
        return ans


            
