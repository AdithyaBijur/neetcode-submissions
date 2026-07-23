class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        patternMap = collections.defaultdict(list)
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        for word in wordList:
            temp = list(word)
            for i in range(0, len(word)):
                temp[i] = '*'
                patternMap[''.join(temp)].append(word)
                temp[i] = word[i]
        
        graph = collections.defaultdict(list)

        for word in wordList:
            temp = list(word)
            for i in range(0, len(word)):
                temp[i] = '*'
                for ele in patternMap[''.join(temp)]:
                    if ele == word:
                        continue
                    graph[word].append(ele)
                temp[i] = word[i]
        
        que = [beginWord]

        level = 0
        visited = set()
        visited.add(beginWord)
        while que:  
            print(que)
            level += 1
            n = len(que)
            for i in range(n):
                word = que.pop(0)
                print(que, graph[word], graph)
                for nei in graph[word]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        visited.add(nei)
                        que.append(nei)
        return 0
                