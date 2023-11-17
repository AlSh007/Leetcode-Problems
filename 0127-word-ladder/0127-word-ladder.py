class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([[beginWord, 1]])
        
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordList:
                        wordList.remove(nextWord)
                        queue.append([nextWord, length + 1])
                        
        return 0