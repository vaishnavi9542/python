class WordDictionary:

    def __init__(self):
        self.trie={}
        

    def addWord(self, word: str) -> None:
        node=self.trie
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]
        node['#']=True


    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i==len(word):
                return '#' in node
            for j in range(i,len(word)):
                ch=word[j]
                if ch=='.':
                    for child in node:
                        if child!='#' and dfs(j+1,node[child]):
                            return True
                    return False
                if ch not in node:
                    return False
                return dfs(i+1,node[ch])
        return dfs(0,self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
