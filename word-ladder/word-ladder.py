class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = collections.deque()
        q.append([beginWord,1])
        while q:
            word,lvl = q.popleft()
            if word == endWord:
                return lvl
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i]+c+word[i+1:]

                    if newword in wordList:
                        wordList.remove(newword)
                        q.append([newword,lvl+1])
        return 0
        