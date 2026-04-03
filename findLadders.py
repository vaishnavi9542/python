class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        parents={}
        level=set([beginWord])
        found=False
        while level and not found:
            next_level=set()
            for word in level:
                if word in wordset:
                    wordset.remove(word)
            for word in level:
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        newword=word[:i]+ch+word[i+1:]
                        if newword in wordset:
                            if newword not in parents:
                                parents[newword]=[]
                            parents[newword].append(word)
                            next_level.add(newword)
                            if newword==endWord:
                                found=True
            level=next_level
        res=[]
        def dfs(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return
            if word not in parents:
                return
            for p in parents[word]:
                dfs(p,path+[p])
        if found:
            dfs(endWord,[endWord])
        return res
