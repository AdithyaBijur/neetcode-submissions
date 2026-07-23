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
        
       
 
        
        que = collections.deque([beginWord])
        visited = set()

        level = 0
        while que:  
            print(que)
            level += 1
            n = len(que)
            for _ in range(n):
                word = que.popleft()
                if word == endWord:
                    return level
                temp = list(word)
                for i in range(0, len(word)):
                    temp[i] = '*'
                    pattern = ''.join(temp)
                    ele = patternMap[pattern]
                    patternMap[pattern] = [] #acts as visited for pattern
                    for e in ele:
                        if e not in visited:
                            visited.add(e)
                            que.append(e)
                    temp[i] = word[i]
        return 0
                