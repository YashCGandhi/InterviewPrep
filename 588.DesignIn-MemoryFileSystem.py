# Using hashmap and lists ( not smart )

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


# Usin Trie ( Very smart i.e me :) )
class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = defaultdict(TrieNode)
        self.is_file = False


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        dirs = path.split("/")
        node  = self.root

        for d in dirs:
            if not d:
                continue
            node = node.children.get(d)
        if node.is_file:
            return [d]
        dirs = [i for i in node.children.keys()]
        if not dirs:
            return dirs
        return sorted(dirs)

    def mkdir(self, path: str) -> None:
        dirs = path.split("/")
        node = self.root

        for dir in dirs:
            if not dir:
                continue
            node = node.children[dir]


    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split("/")
        node  = self.root

        for dir in dirs:
            if not dir:
                continue
            node = node.children[dir]
        node.content += content
        node.is_file = True

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split("/")
        node = self.root

        for dir in dirs:
            if not dir:
                continue
            node = node.children.get(dir)
        return node.content


