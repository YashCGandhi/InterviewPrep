class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)

        # Create a Grahp that connects all the words in the wordList
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                neighbor[pattern].append(word)

        # BFS through the graph to check if I reach the endWord.
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visit:
                            visit.add(neighborWord)
                            q.append(neighborWord)
            res += 1
        return 0

        
