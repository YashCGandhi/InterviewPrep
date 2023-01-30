class FileSystem:

    def __init__(self):
        self.root = {'/':{}}

    def ls(self, path: str) -> List[str]:
        curr = self.root["/"]
        
        if path != "/":
            dirs = path.split("/")
            for dir in dirs[1:]:
                if dir not in curr:
                    return []
                if type(curr[dir]) == list:
                    return [dir]
                curr = curr[dir]
        dirs = []
        for d in curr:
            dirs.append(d)
        return sorted(dirs)

    def mkdir(self, path: str) -> None:
        curr = self.root["/"]
        dirs = path.split("/")
        for dir in dirs[1:]:
            if dir not in curr:
                curr[dir] = {}
            curr = curr[dir]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root["/"]
        dirs = filePath.split("/")
        file = dirs[-1]
        for dir in dirs[1:-1]:
            if dir not in curr:
                curr[dir] = {}
            curr = curr[dir]
        if file not in curr:
            curr[file] = []
        curr[file].append(content)

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root["/"]
        dirs = filePath.split("/")
        file = dirs[-1]
        for dir in dirs[1:-1]:
            if dir not in curr:
                return ""
            curr = curr[dir]
        return "".join(curr[file])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
