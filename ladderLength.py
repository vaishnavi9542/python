class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        q=deque()
        q.append((beginWord,1))
        while q:
            word,step=q.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newword=word[:i]+ch+word[i+1:]
                    if newword in wordset:
                        q.append((newword,step+1))
                        wordset.remove(newword)
        return 0           
        
