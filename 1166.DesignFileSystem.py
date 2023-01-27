# HashMap
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

# HashMap + Trie
class TrieNode:
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name = name
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode("")        

    def createPath(self, path: str, value: int) -> bool:
        comp = path.split("/")

        cur = self.root
        for i in range(1, len(comp)):
            name = comp[i]
            if name not in cur.map:
                if i == len(comp) - 1:
                    cur.map[name] = TrieNode(name)
                else:
                    return False
            cur = cur.map[name]
        if cur.value != -1:
            return False
            
        cur.value = value
        return True

    def get(self, path: str) -> int:
        cur = self.root
        comp = path.split("/")

        for i in range(1, len(comp)):
            name = comp[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value

