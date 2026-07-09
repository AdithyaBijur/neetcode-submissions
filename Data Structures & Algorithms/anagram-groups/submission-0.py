class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)

        for s in strs:
            ans[''.join(sorted(s))].append(s)
        
        anss = []
        for i in ans:
            anss.append(ans[i])
        return anss