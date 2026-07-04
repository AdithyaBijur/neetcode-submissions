class Node:

    def __init__(self,val, isEnd):
        self.val = val
        self.children ={}
        self.isEnd = isEnd
    
    def add(self, node):
        self.children[node.val] = node


class WordDictionary:


    def __init__(self):
        self.root = Node('/', False)
        

    def addWord(self, word: str) -> None:
        
        node = self.root
        for w in range(len(word)):
            if word[w] in node.children:
                node = node.children[word[w]]
            else:
                if w == len(word) - 1:
                    new = Node(word[w], True)
                else:
                    new = Node(word[w], False)
                node.add(new)
                node = new
        
        

    def search(self, word: str) -> bool:

        def search(node, word):
            print(node,word)
            if len(word) == 0:
                return True
            if len(word) == 1:
                if word == '.':
                    for c in node.children:
                        if node.children[c].isEnd:
                            return True
                    else:
                        return False
                else:
                    if word not in node.children:
                        return False
                    else:
                        return node.children[word].isEnd
            if word[0] == '.':
                word = word[1:]
                for c in node.children:
                    if search(node.children[c], word):
                        return True
                return False
            else:
                if word[0] in node.children:
                    return search(node.children[word[0]], word[1:])
                else:
                    return False
        
        return search(self.root, word)
        
