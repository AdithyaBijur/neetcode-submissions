class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = collections.defaultdict(set)
        for word in words:
            for c in word:
                graph[c] = set()

        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i+1]
            ml = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:ml] == w2[:ml]:
                return ""

            for j in range(ml):
                if w1[j] == w2[j]:
                    continue
                graph[w1[j]].add(w2[j])
                break
            


        
        def dfs(char):

            temp = set()
            keys = graph.keys()

            if visited[char] == 2:
                return True
            visited[char] = 1
            for nei in graph[char]:
                if visited[nei] == 1:
                    return False
                if not dfs(nei):
                    return False
            
            visited[char] = 2
            ans.append(char)
            return True
            



        
        visited = collections.defaultdict(int)
        ans = []
        keys = list(graph.keys())
        for char in keys:
            if visited[char] == 0:
                if not dfs(char):
                    return ""
                print(visited)
        return "".join(ans)[::-1]
        