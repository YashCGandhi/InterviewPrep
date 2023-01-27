class FileSystem:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or path in self.paths:
            return False

        i = len(path) - 1
        while i > 0 and path[i] != "/":
            i -= 1
        
        parent = path[:i]
        if len(parent) > 1 and parent not in self.paths:
            return False
        
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
