class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)

        res = []

        def dfs(word):
            for i in range(len(w)):
                if word[:i+1] in word_set and word[i+1:] in word_set:
                    return True
                elif word[:i+1] in word_set and dfs(word[i+1:]):
                    return True
            return False

        for w in words:
            if dfs(w):
                res.append(w)
        return res
