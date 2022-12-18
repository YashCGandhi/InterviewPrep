class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.locations = defaultdict(list)

        for i,w in enumerate(self.wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min_distance = len(self.wordsDict)
        
        idxs_w1, idxs_w2 = self.locations[word1], self.locations[word2]
        i1 = i2 = 0
        # for i1 in idxs_w1:
        #     for i2 in idxs_w2:
        #         if min_distance == 1:
        #             return min_distance
        #         min_distance = min(min_distance, abs(i1 - i2))

        while i1 < len(idxs_w1) and i2 < len(idxs_w2):
            min_distance = min(min_distance, abs(idxs_w1[i1] - idxs_w2[i2]))
            if idxs_w1[i1] < idxs_w2[i2]:
                i1 += 1
            else:
                i2 += 1
        return min_distance
