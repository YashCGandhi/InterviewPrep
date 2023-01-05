class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.pos = -1
        def flatten_list(nested_list):
            for i in nested_list:
                if i.isInteger():
                    self.res.append(i.getInteger())
                else:
                    flatten_list(i.getList())
        flatten_list(nestedList)


    def next(self) -> int:
        self.pos += 1
        return self.res[self.pos]
        
    def hasNext(self) -> bool:
        return self.pos + 1 < len(self.res)
