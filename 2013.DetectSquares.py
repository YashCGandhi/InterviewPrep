class DetectSquares:

    def __init__(self):
        # Here Counter() is used instead of a defaultdict(int) because Counter() does not create a new key if the key is not found in the search, where as a defaultdict() will create a new key.
        # I came across this error where looping through self.ptsCount.item() in the count function, while on this line "res += cnt * self.ptsCount[tuple([x, py])] * self.ptsCount[tuple([px, y])", if one of the two points don't exist then the defaultdict() creates a new point which changes the dimensions of the hashmap which throws an error while running the for loop. (err = dimensions of the map changed while in loop)
        # Thats why Neetcode had used a list "self.pts" to iterate over the points not the defaultdict(int). But, here how you do it!
        self.ptsCount = Counter()
        #self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        #self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for (px, py), cnt in self.ptsCount.items():
            if (abs(x - px) != abs(y - py)) or x == px or y == py:
                continue
            res += cnt * self.ptsCount[tuple([x, py])] * self.ptsCount[tuple([px, y])]

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
